#!/usr/bin/python3
"""
Contains the inherit from function
"""



def inherits_from(obj, a_class):
    """returns true if the object is an instance of a class else false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
