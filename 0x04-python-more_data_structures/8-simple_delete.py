#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    validate = key in a_dictionary
    if validate is True:
        del a_dictionary[key]
    return a_dictionary
