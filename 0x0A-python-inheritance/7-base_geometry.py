#!/usr/bin/python3
"""
Contains the BaseGeometry class
"""

class BaseGeomety:
    """declaring public instance"""
    def area(self):
        """should raise an exception when called"""
        raise Exception("area() is not implmented")

    def integer_validator(self, name, value):
        """should validate the interger when called"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
