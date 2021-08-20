#!/usr/bin/python3
""" This script defines a function find_peak """


def find_peak(list_of_integers):
    """ This function finds a peak in a list of unsorted integers. """
    length = len(list_of_integers)
    if not length:
        return None
    if max(list_of_integers) == min(list_of_integers):
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]\
       and not (list_of_integers[0] < max(list_of_integers)):
        return list_of_integers[0]
    if list_of_integers[length - 1] >= list_of_integers[length - 2]:
        return list_of_integers[length - 1]
    for i in range(1, length - 1):
        if list_of_integers[i] > list_of_integers[i - 1]\
           and list_of_integers[i] > list_of_integers[i + 1]:
            return list_of_integers[i]
