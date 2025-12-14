#!/usr/bin/python3
"""Module that defines the MyList class"""


class MyList(list):
    """Custom list class that inherits from Python's built-in list"""

    def print_sorted(self):
        """Print the list elements sorted in ascending order"""
        print(sorted(self))
