#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_x = 0, 0
    if len(tuple_a) < 2:
        tuple_a = tuple_a + tuple_x
        tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    elif len(tuple_b) < 2:
        tuple_b = tuple_b + tuple_x
        tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    else:
        tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple_c
