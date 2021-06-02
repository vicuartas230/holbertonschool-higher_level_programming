#!/usr/bin/python3
""" This program defines a function save_to_json """
import json


def save_to_json_file(my_obj, filename):
    """ This function writes an Object to a text file,
        using a JSON representation """
    with open(filename, 'w') as new_obj:
        json.dump(my_obj, new_obj)
    new_obj.close()
