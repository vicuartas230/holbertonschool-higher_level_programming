#!/usr/bin/python3
""" This script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter. """
from requests import post
from sys import argv


if __name__ == '__main__':
    if len(argv) < 2:
        dicc = {'q': ""}
    else:
        dicc = {'q': argv[1]}
    req = post('http://0.0.0.0:5000/search_user', data=dicc)
    if len(req.json()) != 0 and type(req.json()) is dict:
        print("[{}] {}".format(req.json().get('id'), req.json().get('name')))
    elif type(req.json()) is not dict:
        print("Not a valid JSON")
    else:
        print("No result")