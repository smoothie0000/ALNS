import itertools
import tsplib95.distances as distances

k = 7

def fix_bounds(permutation, start_node, end_node):
    """
    Fixes the given permutation to the start and end nodes, such that
    it connects up to the remainder of the solution.
    """
    return (start_node,) + permutation + (end_node,)
  

def optimal_subpath(nodes, start_node, end_node):
    """
    Computes the minimum cost subpath from the given nodes, where the 
    subpath is fixed at start_node and end_node.
    """
    def cost(subpath):
        path = fix_bounds(subpath, start_node, end_node)
        
        return sum(distances.euclidean(path[idx][1], path[idx + 1][1])
                   for idx in range(len(path) - 1))

    subpath = min(itertools.permutations(nodes, k), key=cost)

    return fix_bounds(subpath, start_node, end_node)


def post_process(state):
    """
    For each node in the passed-in state, this post processing step 
    computes the optimal subpath consisting of the next k nodes. This
    results in a run-time complexity of about O(n * k!), where n is
    the number of nodes.
    """
    state = state.copy()

    for start_node in state.nodes:
        nodes = []
        node = start_node

        # Determine the next k nodes that make up the subpath starting
        # at this start_node.
        for _ in range(k):
            node = state.edges[node]
            nodes.append(node)
        
        end_node = state.edges[node]

        optimal = optimal_subpath(nodes, start_node, end_node)
        
        # Replace the existing path with the optimal subpath.
        for first, second in zip(optimal, optimal[1:]):
            state.edges[first] = second

    return state