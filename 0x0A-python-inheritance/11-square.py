#!/usr/bin/python3
"""Defines the square of a rectangle"""


class Rectangle:
    """
    A class used to represent a Rectangle

    ...

    Attributes
    ----------
    width : int
        the width of the rectangle
    height : int
        the height of the rectangle

    Methods
    -------
    area():
        Returns the area of the rectangle
    """

    def __init__(self, width, height):
        """
        Parameters
        ----------
        width : int
            The width of the rectangle
        height : int
            The height of the rectangle
        """

        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns
        -------
        int
            The area of the rectangle
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns
        -------
        str
            The square of a rectangle as a string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    A class used to represent a Square

    ...

    Attributes
    ----------
    size : int
        the size of the square

    Methods
    -------
    area():
        Returns the area of the square
    """

    def __init__(self, size):
        """
        Parameters
        ----------
        size : int
            The size of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns
        -------
        int
            The area of the square
        """

        return self.__size ** 2

    def __str__(self):
        """
        Returns
        -------
        str
            The square of a rectangle as a string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer

        Parameters
        ----------
        name : str
            The name of the attribute
        value : int
            The value of the attribute

        Raises
        ------
        TypeError
            If value is not an integer
        ValueError
            If value is not greater than 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
