#!/usr/bin/python3
"""Define class Square that inherits from class Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the size of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
