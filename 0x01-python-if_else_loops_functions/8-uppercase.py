#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if x > 96 and x < 123:
            print("{:c}".format(x - 32), end='')
        else:
            print(str[i], end='')
    print('')
