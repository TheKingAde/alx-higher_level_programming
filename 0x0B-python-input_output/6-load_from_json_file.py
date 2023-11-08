#!/usr/bin/python3
"""Defines function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Read a JSON file and create an object from it's contents"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
