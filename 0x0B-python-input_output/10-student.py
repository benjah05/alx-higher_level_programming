#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Represent class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dict representation of a Student Class
        Args:
            attrs (list): list with dict attributes
        Returns:
            - attributes in attrs list(if attrs is a list)
            - all attributes
        """
        if isinstance(attrs, list):
            attrDict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    attrDict[attr] = self.__dict__[attr]
            return (attrDict);
        else:
            return (self.__dict__)
