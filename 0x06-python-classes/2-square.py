#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): The square's side
        """
        self.__size = size
        if (isinstance(self.__size, int) == False):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
