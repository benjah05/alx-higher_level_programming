#!/usr/bin/python3
"""Import JSON to handle serialization & deserialization"""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object"""
    return (json.dumps(my_obj))
