import math
import networkx as nx
import random


# implement the first algorithm (runtime O(1.42^k * (n + m))) with heuristic
# the heuristic - choose vertex with maximum degree


def run_vertex_cover_alg3_heuristic(graph, k):
    if k < 0:
        return False
    # Rule 1: If G has no edges, return Yes.
    if not list(graph.edges()):
        return True
    # Rule 2: If k=0, return No.
    if k == 0:
        return False
    # Rule 3: If there exists an isolated vertex v, call ALG(G-v,k).
    isolated_vertices = [node for (node, val) in graph.degree() if val == 0]
    if isolated_vertices:
        chosen_vertex = random.choice(isolated_vertices)
        graph_minus_v = graph.copy()
        graph_minus_v.remove_node(chosen_vertex)
        return run_vertex_cover_alg3_heuristic(graph_minus_v, k)
    # Rule 4: If there exists a degree-1 vertex v, call ALG(G-u,k-1) where u is the neighbor of v.
    degree_one_vertices = [node for (node, val) in graph.degree() if val == 1]
    if degree_one_vertices:
        chosen_vertex = random.choice(degree_one_vertices)
        vertex_u = [u for u in graph.neighbors(chosen_vertex)][0]
        graph_minus_u = graph.copy()
        graph_minus_u.remove_node(vertex_u)
        return run_vertex_cover_alg3_heuristic(graph_minus_u, k - 1)
    # Rule 5: If the maximum degree of a vertex in the graph is 2, then solve the problem in polynomial time.
    # basically it's collection of cycles so we have to cover (number of vertices / 2) ceiling.
    # so return "yes"  iff  k >= (number of vertices / 2) ceiling.
    if max([val for (node, val) in graph.degree()]) == 2:
        return k >= sum([math.ceil(len(list(component)) / 2) for component in nx.connected_components(graph)])
    # Rule 6: Pick a vertex v of degree at least 3.
    # i. Call ALG(G-N(v),k-|N(v)|). [Note: |N(v)|≥2.]
    # ii. Call ALG(G-v,k-1).
    # Return Yes iff at least one of the calls returns Yes.
    degree_vertex = [(node, val) for (node, val) in graph.degree()]
    max_degree_vertex = max(degree_vertex, key=lambda x: x[1])
    chosen_vertex = max_degree_vertex[0]
    neighbors_of_chosen_vertex = list(graph.neighbors(chosen_vertex))
    graph_minus_v = graph.copy()
    graph_minus_neighbors_of_v = graph.copy()
    graph_minus_v.remove_node(chosen_vertex)
    graph_minus_neighbors_of_v.remove_nodes_from(neighbors_of_chosen_vertex)
    return run_vertex_cover_alg3_heuristic(graph_minus_v, k - 1) or \
           run_vertex_cover_alg3_heuristic(graph_minus_neighbors_of_v, k - len(neighbors_of_chosen_vertex))
