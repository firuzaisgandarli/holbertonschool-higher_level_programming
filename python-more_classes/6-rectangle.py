#!/usr/bin/python3
"""Rectangle class with instance counter"""


class Rectangle:
    """Defines a rectangle by width and height"""

    # Public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append("#" * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Return a string representation to recreate a new instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message when instance is deleted and decrement counter"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
