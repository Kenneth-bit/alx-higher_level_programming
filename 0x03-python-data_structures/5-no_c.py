#!/usr/bin/python3
def no_c(my_string):
    """Replace c and C in a string"""
    word = ""
    for char in my_string:
        if char != "c" and char != "C":
            word = word + char
    return word
