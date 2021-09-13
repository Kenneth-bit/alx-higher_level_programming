#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    TupA = tuple_a + (0, 0)
    TupB = tuple_b + (0, 0)
    new = TupA[0] + TupB[0], TupA[1] + TupB[1]
    return new
