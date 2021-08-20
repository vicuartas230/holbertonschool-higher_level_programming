#!/usr/bin/python3
""" This script takes in a URL, sends a request to the URL and displays the
    value of the variable X-Request-Id in the response header """
from requests import get
from sys import argv


if __name__ == '__main__':
    if len(argv) < 2:
        exit()
    req = get(argv[1])
    print(req.headers['X-Request-Id'])
