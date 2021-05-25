#!/usr/bin/python3
def text_indentation(text):
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
