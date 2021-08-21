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
    try:
        if len(req.json()) != 0:
            print("[{}] {}".format(req.json()['id'], req.json()['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
