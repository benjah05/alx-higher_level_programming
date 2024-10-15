#!/usr/bin/python3
"""Represent function write_file"""


def write_file(filename="", text=""):
    """Write a string to a text file
    and return number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return (f.write(text))
