#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_x = (0, 0)
    if len(tuple_a) < 2:
        tuple_d = tuple_a + tuple_x
        tuple_c = tuple_d[0] + tuple_b[0], tuple_d[1] + tuple_b[1]
    elif len(tuple_b) < 2:
        tuple_e = tuple_b + tuple_x
        tuple_c = tuple_a[0] + tuple_e[0], tuple_a[1] + tuple_e[1]
    else:
        tuple_c = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return tuple_c
