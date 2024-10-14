#!/usr/bin/python3
"""Represent class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Define Rectangle"""
    def __init__(self, width, height):
        """Initialize width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
    
    def area(self):
        """Implement area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Print with magic method '__str__'"""
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return (string)
