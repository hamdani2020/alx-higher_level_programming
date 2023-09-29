#!/usr/bin/python3
"""Displays the body of the response"""

from sys import argv
import requests

if __name__ = '__main__':
    url = argv[1]

    try:
        u = requests.get(url)
        u.raise_for_status()
        print(u.text)
    except:
        print('Error code: {}'.format(u.status_code))
