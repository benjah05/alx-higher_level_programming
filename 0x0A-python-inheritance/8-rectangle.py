#!/usr/bin/python3
"""Represent class BaseGeometry"""


class BaseGeometry:
    """Define BaseGeometry"""
    def area(self):
        """BaseGeometry with method area
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate "value"
        Args:
            name (str): name
            value (str): value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""Define class rectangle"""


class Rectangle(BaseGeometry):
    """Initialize width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
