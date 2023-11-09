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


class Rectangle(BaseGeometry):
    """Represents a geometric rectangle"""
    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of a triangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the triangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
