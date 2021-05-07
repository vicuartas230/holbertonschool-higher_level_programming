#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    s = []
    for k, v in a_dictionary.items():
        if value == v:
            s.append(k)
    for i in range(len(s)):
        del a_dictionary[s[i]]
    return a_dictionary
