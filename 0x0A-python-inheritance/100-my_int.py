#!/usr/bin/python3
"""Represent clasd MyInt"""


class MyInt(int):
    """MyInt class that inherits from int"""
    def __eq__(self, other):
        """!=: inverted =="""
        return (int(self) != other)

    def __ne__(self, other):
        """==: inverted !="""
        return (int(self) == other)
