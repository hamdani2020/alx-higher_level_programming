#!/usr/bin/python3
"""It displays the value of the X-Request-Id"""


from sys import argv
import urllib.request

if __name__== "__main__":
    with urllib.request.urlopen(argv[1]) as response:
            for header in response.getheaders():
                if header[0] == 'X-Request-Id':
                    print(header[1])
