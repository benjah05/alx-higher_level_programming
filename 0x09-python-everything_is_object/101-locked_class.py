#!/usr/bin/python3
"""Define class LockedClass"""


class LockedClass:
    """Only create a new attribute called first_name"""
    __slots__ = ['first_name']
    def __init__(self):
        pass
