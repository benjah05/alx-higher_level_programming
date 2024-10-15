#!/usr/bin/python3
"""Find the factorial of a number"""


def factorial(n):
    if n == 0:
        return (1)
    return (n * factorial(n - 1))


"""Pascal's triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers
    representing the PAscal's triangle of n
    """
    iterList = []
    pascalList = []
    if n <= 0:
        return (pascalList)
    for i in range(n):
        iterList = []
        for j in range(i + 1):
            iterList.append(factorial(i) // (factorial(j) * factorial(i - j)))
        pascalList.append(iterList)
    return (pascalList)
