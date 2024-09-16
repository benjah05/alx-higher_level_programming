#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print()
    else:
        size = len(matrix)
        for row in matrix:
            for j in range(len(row)):
                print("{:d}".format(row[j]), end=" " if j < size - 1 else "\n")
