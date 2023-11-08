#!/usr/bin/python3
"""Defines a function that raises an Exception"""


class BaseGeometry:
    """This is the BaseGeometry class."""
    def area(self):
        """Calculate the area of the geometric shape"""
        raise Exception("area() is not implemented")
