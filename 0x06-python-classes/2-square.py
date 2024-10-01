#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent a square

    Attributes:
        __size (int): The size of the square's side
    """
    def __init__(self, size=0):
        """Initialize a new squarei

        Args:
            size (int): The square's side
        Raises:
            TypeError: size not an integer
            ValueError: size is less than 0
        """
        self.__size = size
        if (isinstance(self.__size, int) == False):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
