import draw
import repair
import destroy
import tsplib95
import networkx as nx
import numpy.random as rnd
from alns import ALNS, State
from tspState import TspState
import matplotlib.pyplot as plt
from alns.criteria import HillClimbing

SEED = 9876

random_state = rnd.RandomState(SEED)
data = tsplib95.load_problem(r'C:\Users\Administrator\Desktop\ALNS\output\data.tsp')
state = TspState(list(data.node_coords.items()), {})

# alns
alns = ALNS(random_state)

alns.add_destroy_operator(destroy.random_removal)
alns.add_destroy_operator(destroy.path_removal)
alns.add_destroy_operator(destroy.worst_removal)

alns.add_repair_operator(repair.greedy_repair)

# This is perhaps the simplest selection criterion, where we only accept
# progressively better solutions.
criterion = HillClimbing()
initial_solution = repair.greedy_repair(state, random_state)
result = alns.iterate(initial_solution, [3, 2, 1, 0.5], 0.8, criterion,
                      iterations=5000, collect_stats=True)
solution = result.best_state
objective = solution.objective()

# analysis and plot
optimal = 110
print('Best heuristic objective is {0}.'.format(objective))
print('This is {0:.1f}% worse than the optimal solution, which is {1}.'.format(100 * (objective - optimal) / optimal, optimal))
_, ax = plt.subplots(figsize=(12, 6))
result.plot_objectives(ax=ax, lw=2)
draw.draw_graph(data, initial_solution.to_graph())
draw.draw_graph(data, solution.to_graph())
plt.show()

