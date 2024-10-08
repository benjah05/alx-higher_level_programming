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
    """Find the area of the rectangle"""
    def area(self):
        """Calculatee the area of the rectangle
        Returns:
            the area of the rectangle
        """
        return (self.__height * self.__width)
    """Find the perimeter of the rectangle"""
    def perimeter(self):
        """Calculatee the perimeter of the rectangle
        Returns:
            0: if either width or height is 0
            the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)
    """Handle string representation of an object"""
    def __str__(self):
        """Call print() function"""
        return (self.print())
    """Handle string rpresentation with eval(repr(object))"""
    def __repr__(self):
        """Call print() with eval"""
        return (f"Rectangle({self.__width}, {self.__height})")
    """Define print() function"""
    def print(self):
        """Print the rectangle with the character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
        return ("\n".join(rect))
