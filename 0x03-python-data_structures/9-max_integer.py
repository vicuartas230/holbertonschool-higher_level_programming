#!/usr/bin/python3
def max_integer(my_list=[]):
    max_i = 0
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > max_i:
            max_i = i
    return max_i
