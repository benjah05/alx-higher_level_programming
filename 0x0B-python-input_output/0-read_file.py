#!/usr/bin/python3


def read_file(filename=""):
    """Read a file and print it out to stdout"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
