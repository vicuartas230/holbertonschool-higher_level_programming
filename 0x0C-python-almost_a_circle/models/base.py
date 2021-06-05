#!/usr/bin/python3
""" This program defines a class Base """
import json


class Base:
    """ This class will be the “base” of all other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)
