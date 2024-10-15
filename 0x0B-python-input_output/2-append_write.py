#!/usr/bin/python3
def append_write(filename="", text=""):
    """Append a string at the end of a file
    and return the number of characters added
    """
    with open(filename, "a") as f:
        return (f.write(text))