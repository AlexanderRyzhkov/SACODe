from pygraphblas import Matrix


def triangles_count(m):
    matrix = Matrix.from_lists(m[0], m[1], m[2])
    triangle_matrix = matrix.tril()

    return triangle_matrix.mxm(triangle_matrix, mask=triangle_matrix).reduce_int()




