#!/usr/bin/python3
"""It takes in a letter and sends a POST request to the url
"""

from sys import argv
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        a = argv[1]
    else:
        a = ''

    u = requests.post(url, data={'a': a})

    try:
        u = u.json()

        if not u:
            print('No result')
        else:
            print('[{}] {}'.format(u.get('id'), u.get('name')))

    except ValueError:
        print('Not a valid JSON')
