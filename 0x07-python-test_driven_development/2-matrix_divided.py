#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of a list
    Args:
        matrix: the matrix(array of arrays) containing th elements
        div: the number to divide all numbers/ elements with
    Raises:
        TypeError: 
            if div is 0 or not a number(int/float)
            if any element in the matrix is not a number(int/ float)
            if all rows aren't of the same size
        ZeroDivisionError: if div is zero
    """
    result_matrix = []
    if isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix)):
        j = 0
        while matrix[i][j]:
            if isinstance(matrix[i][j], int) or isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            j += 1
        len_row_1 = j
        len_row = j
        if len_row_1 != len_row:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(matrix)):
        if j in rnage(len(matrix)):
            result[i][j] = round(matrix[i][j] / div, 2)
    return (result)
