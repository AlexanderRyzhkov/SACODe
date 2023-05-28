from scipy.sparse import tril, csr_matrix


# m - матрица смежности в виде списка списков


def triangles_count(m):
    matrix = csr_matrix(m)
    triangle_matrix = tril(matrix)

    return int(triangle_matrix.multiply(triangle_matrix * triangle_matrix).sum())




