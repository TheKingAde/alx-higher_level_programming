#!/usr/bin/python3
"""Defines a function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using a JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
