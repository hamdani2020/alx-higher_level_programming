#!/usr/bin/python3
"""This script request n print body, including the error codes"""

from sys import argv
import urllib.request

if __name__ == '__main__':
    url = argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except urllib.error.HTTPError as error:
        print('Erro code: {}'.format(error.code))
