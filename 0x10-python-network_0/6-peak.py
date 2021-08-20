#!/usr/bin/python3
""" This script defines a function find_peak """


def find_peak(list_of_integers):
    """ This function finds a peak in a list of unsorted integers. """
    length = len(list_of_integers)
    if not length:
        return None
    return peak_recursion(list_of_integers, 0, length - 1, length)


def peak_recursion(list, lower, higher, length):
    """ This function does a binary search with recursion """
    middle = lower + (higher - lower) / 2
    middle = int(middle)
    if ((middle == 0 or list[middle - 1] <= list[middle]) and
       (middle == length - 1 or list[middle + 1] <= list[middle])):
        return list[middle]
    elif middle > 0 and list[middle - 1] > list[middle]:
        return peak_recursion(list, lower, (middle - 1), length)
    else:
        return peak_recursion(list, (middle + 1), higher, length)
