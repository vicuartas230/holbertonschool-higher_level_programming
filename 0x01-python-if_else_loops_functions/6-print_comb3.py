#!/usr/bin/python3
for i in range(0, 8):
    for j in range(i + 1, 10):
        print("{:d}".format(i), end='')
        print("{:d}".format(j), end=', ')
print("{:d}{:d}".format(i + 1, j))
