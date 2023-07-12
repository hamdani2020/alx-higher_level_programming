#!/usr/bin/python3
"""
It contains the function "write_file"
"""


def write_file(filename="", text=""):
    """it returns the number of characters in the file"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
