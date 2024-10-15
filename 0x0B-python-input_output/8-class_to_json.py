#!/usr/bin/python3
"""Define class class_to_json"""


def class_to_json(obj):
    """Return a dictionary for JSON serialization"""
    return (obj.__dict__)
