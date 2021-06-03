#!/usr/bin/python3
""" This program defines a class Student """


class Student:
    """ This class defines public attributes of a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict.update({i: getattr(self, i)})
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
