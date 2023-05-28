from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import breadth_first_order

# m - матрица смежности в виде списка списков
# start - индекс начальной вершины

def bfs(m, start):
    matrix = csr_matrix(m)
    return breadth_first_order(matrix, start, directed=True)[0]



