#!/usr/bin/python3
""" This script takes 2 arguments in order to solve this challenge. """
from sys import argv
from requests import get


if __name__ == '__main__':
    req = get("https://api.github.com/repos/{}/{}/commits\
".format(argv[2], argv[1]))
    # print(req.json()[0])
    for i in range(0, 10):
        print("{}: {}".format(req.json()[i]['sha'], req.json()[i]['\
commit']['author']['name']))
