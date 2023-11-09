#!/usr/bin/python3
"""define a class student"""


class Student:
    """
    A class used to represent a Student

    ...

    Attributes
    ----------
    first_name : str
        first name of the student
    last_name : str
        last name of the student
    age : int
        age of the student

    Methods
    -------
    to_json(self, attrs=None):
        Retrieves a dictionary representation of a Student instance
    reload_from_json(self, json):
        Replaces all attributes of the Student instance
    """

    def __init__(self, first_name, last_name, age):
        """
        Parameters
        ----------
        first_name : str
            The first name of the student
        last_name : str
            The last name of the student
        age : int
            The age of the student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Parameters
        ----------
        attrs : list
            List of strings to retrieve specific attribute(s)

        Returns
        -------
        dict
            A dictionary representation of the Student instance
        """

        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance

        Parameters
        ----------
        json : dict
            A dictionary with attributes to replace
        """

        for key, value in json.items():
            setattr(self, key, value)
