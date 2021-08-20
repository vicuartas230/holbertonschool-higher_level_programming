#!/usr/bin/python3
""" This script takes in a URL, sends a request to
    the URL and displays the body of the response. """
from requests import get
from sys import argv


if __name__ == '__main__':
    req = get(argv[1])
    if req.status_code == 200:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))
