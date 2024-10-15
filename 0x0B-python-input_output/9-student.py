#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Represent class Student"""
    def __init__(self, first_name, last_name, age):
        """Initialize public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dict representation of a Student Class"""
        return (self.__dict__)
