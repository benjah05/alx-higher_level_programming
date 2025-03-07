#!/usr/bin/python3
"""import JSON"""
import json


def load_from_json_file(filename):
    """Create an object file from a JSON file"""
    with open(filename, "r") as f:
        return (json.load(f))
