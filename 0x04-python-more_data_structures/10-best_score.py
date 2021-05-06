#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = 0
        for h, i in a_dictionary.items():
            if i > x:
                x = i
        for i, j in a_dictionary.items():
            if j == x:
                return i
        return None
    else:
        return None
