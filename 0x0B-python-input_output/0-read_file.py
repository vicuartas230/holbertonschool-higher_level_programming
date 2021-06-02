#!/usr/bin/python3
""" This program defines a function read_file """

def read_file(filename=""):
    """ This function reads a text file (UTF8) and prints it to stdout """
    with open(filename, 'r') as new:
        reading = new.read()
    print(reading)
    new.close()
