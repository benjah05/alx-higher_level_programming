#!/usr/bin/python3
"""Module math has methods to help calculate area and circumf"""

import math


class MagicClass:
    """Present class MagicClass"""

    def __init__(self, radius=0):
        self.__radius = radius
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius
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
