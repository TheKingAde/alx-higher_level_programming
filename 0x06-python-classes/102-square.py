#!/usr/bin/python3

'''
This script defines a class called Square that represents a square. It has methods to calculate the area of the square and compare squares based on their areas.
'''

class Square:
    '''
    Square is a class that represents a square. It has methods to calculate the area of the square and compare squares based on their areas.
    '''
    def __init__(self, size=0):
        """
        This method initializes a Square instance with a given size.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        This method retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If the provided value is not a number (neither int nor float).
            ValueError: If the provided value is less than 0.
        """
        if not (isinstance(value, float) or isinstance(value, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        This method calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        This method checks if this square is equal to another square (other).

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this square is equal to other, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        This method checks if this square is not equal to another square (other).

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this square is not equal to other, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        This method checks if this square is less than another square (other).

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this square is less than other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        This method checks if this square is less than or equal to another square (other).

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if this square is less than or equal to other, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
         """
         This method checks if this square is greater than another square (other).

         Args:
             other (Square): Another Square instance.

         Returns:
             bool: True if this square is greater than other, False otherwise.
         """
         return self.area() > other.area()

    def __ge__(self, other):
         """
         This method checks if this square is greater than or equal to another square (other).

         Args:
             other (Square): Another Square instance.

         Returns:
             bool: True if this square is greater than or equal to other, False otherwise.
         """
         return self.area() >= other.area()
