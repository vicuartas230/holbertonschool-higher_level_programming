#!/usr/bin/python3
def no_c(my_string):
    string = list(my_string)
    new = ''
    for i in range(0, len(string)):
        if string[i] == 'c' or string[i] == 'C':
            new += ''
        else:
            new += string[i]
    return new
