#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size = len(matrix)
    try:
        for i in range(size):
            for j in range(size):
                print("{:d}".format(matrix[i][j]), end=" " if j < size - 1 else "\n")
    except:
        print()
