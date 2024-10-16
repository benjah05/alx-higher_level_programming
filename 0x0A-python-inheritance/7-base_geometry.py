#!/usr/bin/python3
"""Represent class Geometry"""


class BaseGeometry:
    """Represent classBaseGeometry"""
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
            TypeError:
                - if value is "bool"
                (handle separately because "bool" a subclass of "int")
                - if value is not an integer
            ValueError: if value is less than 0
        """
        if isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
