#!/usr/bin/python3
"""Module that defines a function to save an object to a file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.
    Args:
        my_obj: object to serialize
        filename (str): name of the file to write
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
