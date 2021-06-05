#!/usr/bin/python3
""" This program defines a class Base """
import json
from os import path


class Base:
    """ This class will be the “base” of all other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dicts = []
        if not list_objs:
            with open("{}.json".format(cls.__name__), 'w') as fd:
                json.dump(list_dicts, fd)
        else:
            with open("{}.json".format(cls.__name__), 'w') as fd:
                for obj in list_objs:
                    list_dicts.append(obj.__dict__)
                json.dump(Base.to_json_string(list_dicts), fd)

    @staticmethod
    def from_json_string(json_string):
        list_json = []
        if not json_string:
            return list_json
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(10, 10)
        dummy.update(**dictionary)
        return dummy
