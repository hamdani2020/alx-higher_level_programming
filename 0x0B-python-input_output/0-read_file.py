#!/usr/bin/python3
"""
It constains the read_file function
"""


def read_file(filename=""):
    """read the text file(UF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
