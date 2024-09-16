#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix or not matrix[0]:
        print()
    else:
        for row in matrix:
            for j in range(len(row)):
                separator = 'end=" " if j < len(row) - 1 else if "\n"'
                print("{:d}".format(row[j]), separator)
