#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    n = sorted(a_dictionary)
    for i in n:
        print("{:s}: {}".format(i, a_dictionary[i]))
