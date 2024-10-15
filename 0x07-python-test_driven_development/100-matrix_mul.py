#!/usr/bin/python3
"""matrix_mul function multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Must adhere to the mathematical rules
    Args:
        m_a (list): matrix(list of lists) 1
        m_b (list): matrix 2
    Raises:
        TypeError:
            - if m_a or m_b is not a list
            - if m_a or m_b is not a list of lists
            - if m_a or m_b contain any non-int/ non-float elements
            - if rows in m_a or m_b are not of the same size
        ValueError:
            - if m_a or m_b is empty
            - if m_a and m_b can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_b should contain only integers or floats")
    for row1 in m_a:
        if len(m_a[0]) != len(row1):
            raise TypeError("each row of m_a must be of the same size")
    for row2 in m_b:
        if len(m_b[0]) != len(row2):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return (m_c)
