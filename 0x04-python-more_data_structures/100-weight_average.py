#!/usr/bin/python3
def weight_average(my_list=[]):
    return sum(list(map(lambda x: x[0] * x[1], my_list))) / sum(list(
        map(lambda x: x[1], my_list)))
