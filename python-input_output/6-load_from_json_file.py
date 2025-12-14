#!/usr/bin/python3
"""Module that defines a function to create object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.
    Args:
        filename (str): name of the JSON file
    Returns:
        object: Python data structure
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
