#!/usr/bin/python3
"""Define function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string
    """
    text = ""
    with open(filename, "r") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as f:
        f.write(text)
