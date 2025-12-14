#!/usr/bin/python3
"""Module that defines a function to return JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).
    Args:
        my_obj: object to serialize
    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
