#!/usr/bin/python3
""" This script defines a class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This class inherits from Rectangle class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ This method returns a representation
            of class values in a given format """
        return "[{}] ({}) {}/{} - {}\
".format(__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ This method assigns an argument to each attribute or assigns
            a key/value argument to attributes if args doesn't exist """
        if args:
            names = ['id', 'size', 'x', 'y']
            for value in range(len(args)):
                setattr(self, names[value], args[value])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ This method returns the dictionary representation
            of a Rectangle """
        keys = ['id', 'size', 'x', 'y']
        dicc = {}
        for i in range(len(keys)):
            dicc.update({keys[i]: getattr(self, keys[i])})
        return dicc
