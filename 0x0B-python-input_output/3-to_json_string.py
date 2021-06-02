#!/usr/bin/python3
""" This program defines a function to_json_strong """
import json


def to_json_string(my_obj):
    """ This function returns the JSON representation of an object (string) """
    content = json.dumps(my_obj)
    return content
