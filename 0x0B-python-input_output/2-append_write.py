#!/usr/bin/python3
"""defines a function that appends a string to a text file (utf-8)"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file(utf-8)"""
    with open(filename, mode="a", encoding="utf-8") as file:
        num_characters_added = file.write(text)
    return num_characters_added
