#!/usr/bin/python3
"""
It contains the json string function
"""


import json

def from_json_string(my_str):
    """it returns an object represented by a JSON string"""
    return json.loads(my_str)
