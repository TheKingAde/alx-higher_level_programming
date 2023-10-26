#!/usr/bin/python3
'''
square by: (based on 4-square.py)
'''


class Square:
    def __init__(self, size=0):
        """
        Initialize a Square instance with a given size.

        Args:
            size (float or int, optional): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If the provided value is not a number.
            ValueError: If the provided value is less than 0.
        """
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
