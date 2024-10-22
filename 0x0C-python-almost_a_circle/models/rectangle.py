#!/usr/bin/python3
"""Define class rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the rectangle
        Args:
            width (int): width of the triangle
            height (int): height of the triangle
            x (int): x coordinates of the rectangle
            y (int): y coordinates of the rectangle
            id (Base): id of the rectangle
        Raises:
            TypeError: if either width, height, x or y is not an integer
            ValueError:
                - if either width or height is less than or equal to 0
                - if either x or y is less than 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Set the value of x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Set the value of y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Print the rectangle instance with character '#'
        Addition: handle x and y coordinates
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print("{}".format(' ' * self.__x), end="")
            print("{}".format('#' * self.__width))

    def __str__(self):
        """Magic method for proper string representation"""
        string = "[" + __class__.__name__ + "] " + "(" + str(self.id) + ") "
        string += str(self.__x) + "/" + str(self.__y) + " - "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute if the argument exists
        Args:
            *args: array of arguments
            **kwargs: dictionary of arguments
        """
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        rect_dict = {}
        rect_dict['id'] = self.id
        rect_dict['width'] = self.__width
        rect_dict['height'] = self.__height
        rect_dict['x'] = self.__x
        rect_dict['y'] = self.__y
        return (rect_dict)
