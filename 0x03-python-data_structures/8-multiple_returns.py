#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) > 0):
        tuple_a = len(sentence), sentence[0]
    else:
        tuple_a = len(sentence), None
    return tuple_a
