#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    r = response.read()
    print('Body response')
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
    print("\t- utf8 content: {}".format(r.decode("utf-8")))
