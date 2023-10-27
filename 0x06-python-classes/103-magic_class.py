#!/usr/bin/python3
import math

'''
This script calculates the area and circumference of a circle using a class called MagicClass.
'''

class MagicClass:
    '''
    MagicClass is a class that represents a circle. It has methods to calculate the area and circumference of the circle.
    '''
    def __init__(self, radius=0):
        """
        This method initializes a MagicClass instance with a given radius.

        Args:
            radius (int or float, optional): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If the provided radius is not a number (neither int nor float).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        This method calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        This method calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
