#!/usr/bin/python3
"""Define class Geometry"""


class BaseGeometry:
    """BaseGeometry with method area
    Raises:
        Exception: area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
