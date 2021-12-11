#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    list_1 = set(set_1)
    list_2 = set(set_2)
    return list_1 ^ list_2
