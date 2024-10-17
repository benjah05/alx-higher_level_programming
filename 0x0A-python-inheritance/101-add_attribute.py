#!/usr/bin/python3
"""Define function add_attribute"""


def add_attribute(class_name, attr_name="", attr_value=""):
    """set attribute and check if it exists"""
    setattr(class_name, attr_name, attr_value)
    if hasattr(class_name, attr_name) is False:
        raise TypeError("can't add new attribute")
