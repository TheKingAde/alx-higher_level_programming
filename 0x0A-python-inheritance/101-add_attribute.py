#!/usr/bin/python3
"""Defines a that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters
    ----------
    obj : object
        The object to which the attribute should be added.
    attr_name : str
        The name of the attribute to be added.
    attr_value : any
        The value of the attribute to be added.

    Raises
    ------
    TypeError
        If the attribute cannot be added to the object.
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
