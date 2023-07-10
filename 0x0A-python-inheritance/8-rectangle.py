#!/usr/bin/python3
"""
Contains the Rectangle class and BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of a rectangle"""
    def __init__(self, width, height):
        """instantiating the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", width)
        self.__height = height
