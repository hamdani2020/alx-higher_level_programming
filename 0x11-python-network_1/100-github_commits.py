#!/usr/bin/python3
"""It requests commits via Github API"""

from sys import argv
import requests

if __name__ == '__main__':

    repo = argv[1]
    owner = argv[2]

    url = 'https://api.github.com/repos/{}/{}/\
commits?per_page=10'.format(owner, repo)

u = requests.get(url)
u = u.json()

for commit in u:
    print('{}: {}'.format(commit.get('sha'),
                          commit.get('commit').get('author').get('name')))
