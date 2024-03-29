#!/usr/bin/python3
""" displays the value of the variable X-Request-Id in the response header """
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    the_id = r.headers.get("X-Request-Id")
    print(the_id)
