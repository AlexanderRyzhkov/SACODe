from igraph import Graph


"""
m - матрица смежности в виде списка списков
start - индекс начальной вершины

на выходе список, который содержит длину кратчайшего пути от начала до вершины с номером n в соотвествующем индексе вектора
"""


def sssp(m, start):
    matrix = Graph.Weighted_Adjacency(m)
    return matrix.shortest_paths(start, weights=matrix.es["weight"])[0]



