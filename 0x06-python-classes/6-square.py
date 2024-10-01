#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Represent class Square
    Attributes:
        __size (int): side length of a square
        __position (tuple): tuple of square coordinates
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        Args:
            size (int): side length of the square
            position (tuple): square coordinates
        """
        self.__size = size
        self.__position = position
    """Use getter method"""
    @property
    def size(self):
        """Get the value of size
        Returns:
             The value of size
        """
        return (self.__size)
    """Use setter method"""
    @size.setter
    def size(self, value):
        """Set the value of size
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
    """Use getter method for coordinates"""
    @property
    def position(self):
        """Get the square's coordinates
        Returns:
            The square's coordinates
        """
        return (self.__position)
    """Use setter method for coordinates"""
    @position.setter
    def position(self, value):
        """Set value for square's coordinates
        Args:
            value (int): value(tuple) to set to position
        Raises:
            TypeError: if position is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """The ares of the square"""
    def area(self):
        """Calculate the area of the square
        Returns:
            The area of the square
        """
        return (self.__size ** 2)
    """Print the value of position(coordinates)"""
    def my_print(self):
        """Print the position tuple of coordinates
        Args:
            position (tuple): tuple of the square's coordinates
        """
        if (self.__size == 0):
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
