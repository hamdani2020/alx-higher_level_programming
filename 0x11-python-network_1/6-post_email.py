#!/usr/bin/python3
"""This script makes a POST a request"""

from sys import argv
import requests

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    u = requests.post(url, data={'email': email})
    print(u.text)
