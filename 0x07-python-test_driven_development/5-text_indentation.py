#!/usr/bin/python3
""" This program is used to test
    all posible special cases
    in function text_dentation """


def text_indentation(text):
    """ This function prints a text with 2 new lines
        after each of these characters: '.', '?' and ':'
        text is a string """
    comp = 1
    if type(text) is not str:
        raise TypeError("text must be a string")
    separator = '.:?'
    letter = 0
    while letter in range(len(text)):
        try:
            for char in separator:
                if text[letter] == char:
                    comp = 0
                    print("{}{}".format(text[letter], '\n'))
                    letter += 1
                    break
            if text[letter + 1] and text[letter + 1] != ' \
' and text[letter] == ' ' and not comp:
                comp = 1
                letter += 1
            elif text[letter] == ' ' and text[letter + 1] == ' ':
                comp = 0
                letter += 1
                continue
            elif comp:
                print("{}".format(text[letter]), end='')
                letter += 1
        except IndexError:
            if text[letter] != ' ':
                print("{}".format(text[letter]), end='')
            break
