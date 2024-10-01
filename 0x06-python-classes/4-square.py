#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent class Square
    Attributes:
        __size (int): The size of a square
    """
    def __init__(self, size=0):
        """Initialize the square
        Args:
            size (int): The square's side
        """
        self.__size = size
    @property
    def size(self):
        """Get the value of size
        Returns:
            The integer value of size
        """
        return (self.__size)
    @size.setter
    def size(self, value):
        """Set the value of self.__size
        Args:
            value (int): the size of a square's side
        Raises:
            TypeError: if size is not an integer
            ValueError: if the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    """Find the area of the square"""
    def area(self):
        """Calcualte the area
        Returns:
            The area of the square
        """
        return (self.__size ** 2)
