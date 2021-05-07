#!/usr/bin/python3
def weight_average(my_list=[]):
    return 0 if not len(my_list) else sum(list(map(
        lambda x: x[0] * x[1], my_list))) / sum(list(
            map(lambda x: x[1], my_list)))
