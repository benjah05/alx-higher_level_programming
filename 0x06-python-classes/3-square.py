#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent a square
    Attributes:
        __size (int): the square's side
    """
    def __init__(self, size=0):
        """Initialize the new square
        Args:
            size (int): the side length of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
    """Find the area of the square"""
    def area(self):
        """Method used to return the area of a square
        Returns:
            The area of a square
        """
        return (self.__size ** 2)
