#!/usr/bin/python3
""" script that POST email into a URL """
import urllib.request
import urllib.parse
import sys


if __name__ == '__main__':
    email = urllib.parse.urlencode({"email": sys.argv[2]})
    email = email.encode('ascii')
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
