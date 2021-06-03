#!/usr/bin/python3
""" This program defines a function class_to_json """
import json


def class_to_json(obj):
    """ This function returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for
        JSON serialization of an object """
    return json.dumps(obj.__dict__)
