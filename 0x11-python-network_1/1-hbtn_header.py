#!/usr/bin/python3
""" script that get the 'X-Request-Id' Data from the header """
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        r = response.headers
        the_id = r.get('X-Request-Id')
        print(the_id)
