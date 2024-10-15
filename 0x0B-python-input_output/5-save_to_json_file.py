#!/usr/bin/python3
"""import JSON and handle serizalization/ deserialization"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
