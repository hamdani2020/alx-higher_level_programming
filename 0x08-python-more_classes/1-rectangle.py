#!/usr/bin/python3
"""
Define a class rectangle
"""

class Rectangle:
    """Representation of a Rectangle."""
    def __init__(self, width=0, height=0):
        """Initialzes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for the private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if type(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if type(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


