#!/usr/bin/python3
def pascal_triangle(n):
    """Return a list of lists of integers
    representing the PAscal's triangle of n
    """
    pascalList = []
    if n <= 0:
        return (pascalList)
    for i in range(n):

