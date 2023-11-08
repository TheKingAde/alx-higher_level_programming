#!/usr/bin/python3
"""defines a function that returns the dictionary description"""


def class_to_json(obj):
    """
    Return a dictionary description with simple data structures for JSON

    Args:
        obj (object): An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the serialized attributes
    """
    obj_dict = vars(obj)
    serialized_dict = {}

    for key, value in obj_dict.items():
        if isinstance(value, (str, int, bool, list, dict)):
            serialized_dict[key] = value

    return serialized_dict
