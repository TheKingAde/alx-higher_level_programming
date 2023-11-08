#!/usr/bin/python3
"""defines a function that returns an object (Python data structure)"""
import json


def from_json_string(my_str):
    """Return a python data structure represented by a JSON string"""
    return json.loads(my_str)
