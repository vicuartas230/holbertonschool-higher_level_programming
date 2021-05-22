#!/usr/bin/python3
""" This program blocks creating new instance attributes """


class LockedClass:
    """ The class to block """
    __slots__ = 'first_name'
