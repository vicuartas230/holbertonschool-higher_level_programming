#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cpy = []
    for i in range(len(my_list)):
        if i == idx:
            list_cpy.append(element)
        else:
            list_cpy.append(my_list[i])
    return list_cpy
