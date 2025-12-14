#!/usr/bin/python3
"""Module that defines a function to return dictionary description for JSON serialization"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization of an object.
    Args:
        obj: instance of a Class
    Returns:
        dict: dictionary description of obj
    """
    return obj.__dict__
