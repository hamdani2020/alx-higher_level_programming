#!/usr/bin/python3
"""
Contains the class BaseGeomatry and Rectangle
"""


class BaseGeometry:
    """Declaring a public instance"""
    def area(self):
        """rasies an exception when called"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """validates when the integer is greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represens the rectangle"""
    def __init__(self, width, height):
        """instantiation the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """it returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
