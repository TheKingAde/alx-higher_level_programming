#!/usr/bin/python3
'''
defines a square by: (based on 6-square.py)
'''


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with a given size and position.

        Args:
            size (int, optional): The size of the square. Default is 0.
            position (tuple, optional): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

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
        Retrieve the position of the square.

        Returns:
            tuple: position of the square as a tuple of two +ve integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): new position

        Raises:
            TypeError: If the provided value is not a tuple of two +ve int
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) for i in value) or \
           not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using '#' characters with proper positioning.

        If size is equal to 0, print an empty line.
        The position attribute is used to control the number of spaces before '#'
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
        Return a string representation of the square with the specified position.

        Returns:
            str: A string representation of the square with proper positioning.
        """
        square_str = ""
        if self.__size == 0
            return square_str
        else:
            for _ in range(self.__position[1]):
                square_str += "\n"
            for _ in range(self.__size):
                square_str += " " * self.__position[0] + "#" * self.__size + "\n"
        return square_str[:-1]  # Remove the trailing newline
