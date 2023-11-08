#!/usr/bin/python3
"""Defines a function that raises an Exception"""


class BaseGeometry:
    """This is the BaseGeometry class."""
    def area(self):
        """Calculate the area of the geometric shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the integer value.

        Args:
            name(str): name of value being evaluated
            value(int): value to be validated.

        Raises:
            TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
