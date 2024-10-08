#!/usr/bin/python3
"""Represent class Rectangle"""


class Rectangle:
    """Initiialize the Rectangle
    Attributes:
        width (int): the width of a rectangle
        height (int): the height of a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    """width getter"""
    @property
    def width(self):
        """Get the value of width
        Returns:
            width of the rectangle
        """
        return (self.__width)
    """width setter"""
    @width.setter
    def width(self, value):
        """Set the value of the width
        Args:
            value (int): data to be assigned to the width
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    """height getter"""
    @property
    def height(self):
        """Get the value of height
        Returns:
            height of the rectangle
        """
        return (self.__height)
    """height setter"""
    @height.setter
    def height(self, value):
        """Set the value of the heught
        Args:
            value (int): data to be assigned to the height
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
