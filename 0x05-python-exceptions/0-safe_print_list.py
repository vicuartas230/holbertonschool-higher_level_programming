#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0
    for i in range(x):
        if my_list[i]:
            print("{}".format(my_list[i]), end='')
            printed += 1
        else:
            return printed
    print('')
    return printed
