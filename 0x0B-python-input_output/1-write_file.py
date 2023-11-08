#!/usr/bin/python3
""" defines a function that writes to a text file"""


def write_file(filename="", text=""):
    """write a string to a text file and return number written"""
    with open(filename, mode='w', encoding="utf-8") as file:
        num_characters_written = file. write(text)
    return num_characters_written
