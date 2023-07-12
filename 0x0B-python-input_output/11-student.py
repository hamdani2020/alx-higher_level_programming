#!/usr/bin/python3
"""
It contains the Student class
"""

class Student:
    """representation of student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation of public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """it returns a dictionary representation of a student instance with attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
            return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
