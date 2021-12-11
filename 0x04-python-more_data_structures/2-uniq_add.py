#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for number in set(my_list):
        total += number
    return total
