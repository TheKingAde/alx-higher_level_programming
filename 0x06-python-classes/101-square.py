#!/usr/bin/python3

'''
This script defines a class called Square that represents a square. It has methods to calculate the area of the square, print the square with proper positioning, and return a string representation of the square.
'''

class Square:
    '''
    Square is a class that represents a square. It has methods to calculate the area of the square, print the square with proper positioning, and return a string representation of the square.
    '''
    def __init__(self, size=0, position=(0, 0)):
        """
        This method initializes a Square instance with a given size and position.

        Args:
            size (int, optional): The size of the square. Default is 0.
            position (tuple, optional): The position of the square in 2D space as a tuple of two integers. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        This method retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This method sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        This method retrieves the position of the square.

        Returns:
            tuple: The position of the square as a tuple of two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This method sets the position of the square.

        Args:
            value (tuple): The new position of the square as a tuple of two positive integers.

        Raises:
            TypeError: If the provided value is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """
        This method calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        This method prints the square using '#' characters with proper positioning.

        If size is equal to 0, it prints an empty line. The position attribute is used to control the number of spaces before '#'.
        
         Returns:
            None
       """
       if self.__size == 0:
           print()
       else:
           for _ in range(self.__position[1]):
               print()
           for _ in range(self.__size):
               print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
       """
       This method returns a string representation of the square with proper positioning.

       Returns:
           str: A string representation of the square with '#' characters and proper positioning. If size is equal to 0, it returns an empty string.
       """
       if self.__size == 0:
           return ""
       else:
           result = "\n" * self.__position[1]
           result += "\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size))
           return result
