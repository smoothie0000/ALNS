import networkx as nx
import matplotlib.pyplot as plt

# draw
def draw_graph(data, graph, only_nodes=False):
  """
  Helper method for drawing TSP (tour) graphs.
  """
  fig, ax = plt.subplots(figsize=(12, 6))

  func = nx.draw_networkx

  if only_nodes:
      func = nx.draw_networkx_nodes

  func(graph, data.node_coords, node_size=25, with_labels=False, ax=ax)
