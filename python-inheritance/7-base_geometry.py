#!/usr/bin/python3
"""Module that defines the BaseGeometry class with area and integer_validator methods"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation"""

    def area(self):
        """Raise an Exception indicating area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is an integer greater than 0.
        Args:
            name (str): name of the variable
            value (int): value to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
