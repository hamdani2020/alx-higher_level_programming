#!/usr/bin/python3
"""Displays the value of the variable X-Request-Id"""

from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    u = requests.get(url)
    u = u.headers
    print(u.get('X-Request-Id'))
