#!/usr/bin/python3
"""Define class square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the square
        Args:
            size (int): size of the square
            x (int): x coordinates of the rectangle
            y (int): y coordinates of the rectangle
            id (Rectangle): id of the square
        Raises:
            TypeError: if either size, x or y is not an integer
            ValueError:
                - if size os less than or equal to 0
                - if either x or y is less than 0
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return the value of width"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the value of weight
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")"""
        self.width = value
        self.height = value

    def display(self):
        """Print the square instance with character '#'
        Addition: handle x and y coordinates
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            print("{}".format(' ' * self.x), end="")
            print("{}".format('#' * self.width))

    def __str__(self):
        """Magic method for proper string representation"""
        string = "[" + __class__.__name__ + "] " + "(" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width)
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
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        sqr_dict = {}
        sqr_dict['id'] = self.id
        sqr_dict['size'] = self.size
        sqr_dict['x'] = self.x
        sqr_dict['y'] = self.y
        return (sqr_dict)
