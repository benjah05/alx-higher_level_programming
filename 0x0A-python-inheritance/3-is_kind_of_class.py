#!/usr/bin/python3
"""Define function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of,
    or if the object is an instance of a class that
    inheritance from
    """
    def is_kind_of_class(obj, a_class):
        if isinstance(obj, a_class):
            return (True)
        else:
            return (False)
