#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of a list
    Args:
        matrix: the matrix(array of arrays) containing th elements
        div: the number to divide all numbers/ elements with
    Raises:
        TypeError: 
            - if div is 0 or not a number(int/float)
            - if any element in the matrix is not a number(int/ float)
            - if all rows aren't of the same size
        ZeroDivisionError: if div is zero
    Returns:
        list: result_matrix, the original matrix with its elements divided by div
    """
    result_matrix = []
    row_length = len(matrix[0])
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        result_matrix.append(new_row)
    return (result_matrix)
