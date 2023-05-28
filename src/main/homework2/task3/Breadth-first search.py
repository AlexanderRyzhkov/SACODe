from igraph import Graph




def bfs(m, start):
    matrix = Graph.Adjacency(m)
    return matrix.bfs(start)[0]




