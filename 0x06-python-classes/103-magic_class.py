#!/usr/bin/python3
import math
"""Define class MagicClass"""


class MagicClass:
    """Present class MagicClass
    Attributes:
        __radius (int): radius of a circle
    """
    def __init__(self, radius):
        self.__radius = radius
    """Calculate the area of a circle"""
    def area(sels, radius):
        """Find the ares of a circle
        Returns:
            The area
        """
        return ((self.__radius ** 2) * math.pi)
    """Calculate the circumf of a circle"""
    def circumference(self, radius):
        """Find circumference
        Returns:
            circumf of the circle
        """
        return ((math.pi * 2) * self.__radius)

