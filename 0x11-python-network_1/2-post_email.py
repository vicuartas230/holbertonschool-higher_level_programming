#!/usr/bin/python3
""" This script takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter, and displays
    the body of the response (decoded in utf-8) """
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == '__main__':
    dictionary = {
        'email': argv[2]
    }
    data = urlencode(dictionary)
    data = data.encode('utf-8')
    req = Request(argv[1], data)
    with urlopen(req) as response:
        print(response.read())
