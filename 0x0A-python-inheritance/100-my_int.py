#!/usr/bin/python3
'''define class MyInt function'''


class MyInt(int):
    """
    A class that inherits from int
    inequality (!=) operators.

    Attributes:
        value (int): The integer value of the MyInt instance.

    Methods:
        __init__(self, value):
            Initializes a new MyInt instance with the specified integer value.

        __eq__(self, other):
            Overrides the equality operator (==) to return the inverted result

        __ne__(self, other):
            Overrides the inequality operator (!=) to return the inverted result
    """

    def __init__(self, value):
        """
        Initializes a new MyInt instance with the specified integer value.

        Args:
            value (int): The integer value to assign to the MyInt instance.
        """
        self.value = value

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to return the inverted result

        Args:
            other: The value or object to compare with the MyInt instance.

        Returns:
            bool: True if the values are not equal; otherwise, False.
        """
        return self.value != other

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to return the inverted result

        Args:
            other: The value or object to compare with the MyInt instance.

        Returns:
            bool: True if the values are equal; otherwise, False.
        """
        return self.value == other
