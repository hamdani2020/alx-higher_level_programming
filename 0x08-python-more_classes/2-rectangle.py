#!/usr/bin/python3
"""
Defines a class Rectangle
"""

class Rectangle:
    """Representing the rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if type(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if type(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """It returns the area of the rectangle"""
        return self.__height * self__width

    def perimeter(self):
        """It returns theh perimeter of the rectangle"""
        if self.__width or self.__height ==0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
