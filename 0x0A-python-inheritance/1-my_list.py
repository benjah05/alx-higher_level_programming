#!/usr/bin/python3
"""Define class MyList"""


class MyList(list):
    """subclass of list"""

    def print_sorted(self):
        """Initialize a list"""
        sorted_list = sorted(self)
        print(sorted_list)
