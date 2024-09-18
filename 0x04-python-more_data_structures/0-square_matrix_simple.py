#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sum = []
    for row in matrix:
        total = list(map(lambda x: x**2, row))
        matrix_sum.append(total)
    return (matrix_sum)
