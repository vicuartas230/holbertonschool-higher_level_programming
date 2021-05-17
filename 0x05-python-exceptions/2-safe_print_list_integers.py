#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end='')
            printed += 1
        print('')
        return printed
    except ValueError:
        print('')
        return printed
