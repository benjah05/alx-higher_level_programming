#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent class Square
    Attributes:
        __size (int): the side length of the square
    """
    def __init__(self, size=0):
        """Initialize size
        Args:
            size (int): the side length of the square
        """
        self.__size = size
    """Get the value of size"""
    @property
    def size(self):
        """Set the value of size
        Returns:
            The value of size
        """
        return (self.__size)
    """Set the value of size"""
    @size.setter
    def size(self, value):
        """Set the value of value
        Args:
            value (int): value to set to size
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    """Find the area of the square"""
    def area(self):
        """Calculate the area
        Returns:
            The area of the square
        """
        return (self.__size ** 2)
    """Print the value of size"""
    def my_print(self):
        """Print the value of size
        Args:
            size (int): side length of a square
        """
        if (self.__size == 0):
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
