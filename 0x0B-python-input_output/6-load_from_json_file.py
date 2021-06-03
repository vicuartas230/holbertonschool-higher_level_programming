#!/usr/bin/python3
""" This program efines a function load_from_json_file """
import json


def load_from_json_file(filename):
    """ This function creates an Object from a “JSON file” """
    with open(filename, 'a') as new:
        return json.load(new)
