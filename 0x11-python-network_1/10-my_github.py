#!/usr/bin/python3
"""Request from GitHub API"""

from sys import argv
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = argv[1]
    token = argv[2]
    headers = {'Authorization': 'token {}'.format(token)}

    u = requests.get(url, headers=headers)
    print(u.json().get('id'))
