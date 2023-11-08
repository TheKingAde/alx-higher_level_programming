#!/usr/bin/python3
"""defines a function that resturns the JSON representation of an object"""


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string"""
    return json.dumps(my_obj)
