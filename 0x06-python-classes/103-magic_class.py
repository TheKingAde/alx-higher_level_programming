#!/usr/bin/python3
import math
'''
calculate the area and circumference of a circle
'''


class MagicClass:
    '''MagicClass for a  Python bytecode'''
    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float, optional): The radius of the circle.

        Raises:
            TypeError: If the provided radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate and return the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
