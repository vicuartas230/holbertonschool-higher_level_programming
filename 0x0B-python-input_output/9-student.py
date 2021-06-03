#!/usr/bin/python3
""" This program defines a class Student """


class Student:
    """ This class defines public attributes of a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
