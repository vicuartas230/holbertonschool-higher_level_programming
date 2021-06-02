#!/usr/bin/python3
""" This program defines a function from_json_string """
import json


def from_json_string(my_str):
    """ This function returns an object (Python data structure)
        represented by a JSON string """
    obj_str = json.loads(my_str)
    return obj_str
