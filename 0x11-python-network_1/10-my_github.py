#!/usr/bin/python3
""" This script takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id """
from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth


if __name__ == '__main__':
    req = get('https://api.github.com/user', verify=False,
              auth=HTTPBasicAuth(argv[1], argv[2]))
    print(req.json()['id'])
