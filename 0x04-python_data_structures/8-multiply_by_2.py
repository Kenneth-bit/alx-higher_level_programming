#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for i in a_dictionary:
        mul = 2 * a_dictionary[i]
        new[i] = mul
    return new
