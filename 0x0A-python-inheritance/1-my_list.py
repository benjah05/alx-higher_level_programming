#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):
    """Print sorted list"""
    def print_sorted(self):
        print(sorted(self))
