import numpy.random as rnd
from tspState import TspState
import repair
import networkx as nx
import matplotlib.pyplot as plt

SEED = 9876

import tsplib95

data = tsplib95.load_problem(r'C:\Users\Administrator\Desktop\ALNS\output\data.tsp')
random_state = rnd.RandomState(SEED)
state = TspState(list(data.node_coords.items()), {})

initial_solution = repair.greedy_repair(state, random_state)

print("Initial solution objective is {0}.".format(initial_solution.objective()))


def draw_graph(graph, only_nodes=False):
  """
  Helper method for drawing TSP (tour) graphs.
  """
  fig, ax = plt.subplots(figsize=(12, 6))

  func = nx.draw_networkx

  if only_nodes:
      func = nx.draw_networkx_nodes

  func(graph, data.node_coords, node_size=25, with_labels=False, ax=ax)

draw_graph(initial_solution.to_graph())
plt.show()