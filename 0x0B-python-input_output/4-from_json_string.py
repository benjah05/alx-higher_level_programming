#!/usr/bin/python3
"""Handle serialization & deserialization with JSON"""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string"""
    return (json.loads(my_str))
