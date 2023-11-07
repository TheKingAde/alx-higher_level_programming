#!/usr/bin/python3
'''define inherits_from function'''


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
