#!/usr/bin/python3
import math
"""Define class MagicClass"""


class MagicClass:
    """Present class MagicClass
    Attributes:
        __radius (int): radius of a circle"""
    def __init__(self, radius):
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        return (None)
    """Calculate the area of a circle"""
    def area(self):
        """Find the ares of a circle
        Returns:
            The area
        """
        return ((self.__radius ** 2) * math.pi)
    """Calculate the circumf of a circle"""
    def circumference(self):
        """Find circumference
        Returns:
            circumf of the circle
        """
        return ((math.pi * 2) * self.__radius)

