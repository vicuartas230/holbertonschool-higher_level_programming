#!/usr/bin/python3
""" This script fetches https://intranet.hbtn.io/status """
from requests import get


if __name__ == '__main__':
    req = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
