#!/usr/bin/python3
""" This script defines a class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} {}\
".format(__class__.__name__, self.id, self.x, self.y, self.width)
