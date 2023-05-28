from igraph import Graph




def triangles_count(m): #m - матрица смежности в виде списка списков
    matrix = Graph.Adjacency(m)
    return len(matrix.cliques(3, 3)) #найти все циклы, где мин колво вершин 3 и максимальным тоже 3 - короче, треугольники




