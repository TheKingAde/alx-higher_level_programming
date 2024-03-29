#!/usr/bin/python3
"""defines a function that adds all arguments to a Python list"""


import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_items_to_list_and_save(args, filename):
    """
    Add command-line arguments to a Python list and save it to a JSON file.

    Args:
        args (list): A list of command-line arguments to be added.
        filename (str): The name of the JSON file for saving the list.

    Returns:
        None
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)
