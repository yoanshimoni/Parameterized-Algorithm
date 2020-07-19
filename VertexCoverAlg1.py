import math
import networkx as nx
import random


# implement the first algorithm (runtime O(2^k * (n + m)))

def run_vertex_cover_alg_1(graph, k):
  # Rule 1: If G has no edges, return Yes.
  if not list(graph.edges()):
    return True
  # Rule 2: If k=0, return No.
  elif k == 0:
    return False
  #  Rule 3. Pick an edge {u,v}.
  # i. Call ALG(G-u,k-1).
  # ii. Call ALG(G-v,k-1).
  # Return Yes iff at least one of
  # the calls returns Yes.
  else:
    chosen_edge = random.choice(list(graph.edges))
    graph_minus_v = graph.copy()
    graph_minus_v.remove_node(chosen_edge[0])
    graph_minus_u = graph.copy()
    graph_minus_u.remove_node(chosen_edge[1])
    return run_vertex_cover_alg_1(graph_minus_v, k - 1) or \
           run_vertex_cover_alg_1(graph_minus_u, k - 1)
