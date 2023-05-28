from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import bellman_ford

# m - матрица смежности в виде списка списков
# start - индекс начальной вершины

def sssp(m, start):
    matrix = csr_matrix(m)
    return bellman_ford(csgraph=matrix, directed=True, indices=start, return_predecessors=False)




