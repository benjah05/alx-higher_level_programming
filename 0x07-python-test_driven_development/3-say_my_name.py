#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Print someone's full name
    Args:
        first_name: the first name
        last_name: the last/ family name
    Raises:
        TypeError: if first_name or last_name isn't a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
