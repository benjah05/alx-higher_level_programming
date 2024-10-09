#!/usr/bin/python3
"""Represent class Rectangle"""


class Rectangle:
    """Public class atrributes"""
    number_of_instances = 0
    print_symbol = "#"
    """Initiialize the Rectangle
    Attributes:
        width (int): the width of a rectangle
        height (int): the height of a rectangle
        number_of_instances (int): instance count
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1
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
        symbol = str(self.print_symbol)
        for i in range(self.__height):
            rect.append(symbol * self.__width)
        return ("\n".join(rect))
    def __del__(self):
        """Print message after instance deletion
           And count number of instances deleted
        """
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare 2 rectangles
        Return:
            Biggest rectangle
            rect_1: if both rectangles are equal
        Raises:
            TypeError: if any arg isn't of Rectangle type
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
