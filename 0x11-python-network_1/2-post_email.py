#!/usr/bin/python3
"""This script makes a POST request"""

from sys import argv
import urllib.request

if __name__ == '__main__':
    url = argv[1]
    email = {'email': argv[2]}

    email = urllib.parse.urlencode(email)
    email = email.encode('utf-8')

    request = urllib.request.Request(url, email)

    with urllib.request.urlopen(request) as response:
        response = response.read()
        response = response.decode('utf-8')
        print(response)
