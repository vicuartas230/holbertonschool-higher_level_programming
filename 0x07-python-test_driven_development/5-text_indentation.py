#!/usr/bin/python3
""" This program is used to test
    all posible special cases
    in function text_dentation """


def text_indentation(text):
    """ This function prints a text with 2 new lines
        after each of these characters: '.', '?' and ':'
        text is a string """
    if type(text) is not str:
        raise TypeError("text must be a string")
    separator = '.:?'
    letter = 0
    while letter in range(len(text)):
        for char in separator:
            if text[letter] == char:
                print("{}{}".format(text[letter], '\n'))
                letter += 2
                break
        print("{}".format(text[letter]), end='')
        letter += 1
