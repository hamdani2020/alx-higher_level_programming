#!/usr/bin/python3
"""
Defines the rectangle class
"""


class Rectangle:
    """representing the rectangle class"""
    def __init__(self, width=0, height=0):
        """Instantiation of the instance class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """instantiating the getter private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """instantiating the setter private instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Instantiating the getter private instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """instantiating the setter private instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """It returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """It returns the perimeter of the rectangle"""
        if self.__width or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns printable string representing the rectangle"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width for i in range(self.__height))
        return string

    def __repr__(self):
        """it returns a string representatoin of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
