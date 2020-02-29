import tsplib95
import networkx as nx

import matplotlib.pyplot as plt

data = tsplib95.load_problem(r'C:\Users\Administrator\Desktop\ALNS\output\data.tsp')
print(list(data.node_coords.items()))
# solution = tsplib95.load_solution(r'C:\Users\Administrator\Desktop\ALNS\output\init_solution.opt.tour')
# optimal = data.trace_tours(solution)[0]

# print('Total optimal tour length is {0}.'.format(optimal))

# def draw_graph(graph, only_nodes=False):
#   """
#   Helper method for drawing TSP (tour) graphs.
#   """
#   fig, ax = plt.subplots(figsize=(12, 6))

#   func = nx.draw_networkx

#   if only_nodes:
#       func = nx.draw_networkx_nodes

#   func(graph, data.node_coords, node_size=25, with_labels=False, ax=ax)

# draw_graph(data.get_graph(), True)
# plt.show()