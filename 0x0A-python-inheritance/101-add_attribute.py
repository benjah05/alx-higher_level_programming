#!/usr/bin/python3
"""Define function add_attribute"""


def add_attribute(class_name, attr_name="", attr_value=""):
    """set attribute and check if it exists
    Args:
        class_name (obj): an object of the class
        attr_name (str): new attribute name
        attr_value (str): new attribute value
    Raises:
        TypeError: if attribute csn not be created
    """
    if not hasattr(class_name, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(class_name, attr_name, attr_value)
