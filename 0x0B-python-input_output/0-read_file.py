#!/usr/bin/python3
"""defines a function that reads file"""


def read_file(filename=""):
    """Reads and prints a text file (UTF-8) to stdout."""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
