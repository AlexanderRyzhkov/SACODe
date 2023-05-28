from pygraphblas import Matrix, Vector, INT64


"""
m - информация о каждом ребре в виде списка из 3 списков: 
0 - начальные вершины, 1 - конечные вершины, 2 - веса.
start - индекс начальной вершины.

на выходе вектор, который содержит длину кратчайшего пути от начала до вершины с номером n в соответсвующем индексе
"""


def sssp(m, start):
    matrix = Matrix.from_lists(m[0], m[1], m[2])
    result = Vector.sparse(matrix.type, matrix.nrows)
    result[start] = 0

    for i in range(matrix.nrows):
        result.min_plus(matrix, out=result, accum=INT64.min)
        #https://en.wikipedia.org/wiki/Min-plus_matrix_multiplication
    return result



