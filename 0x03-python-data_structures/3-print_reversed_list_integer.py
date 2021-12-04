#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Prints the list elements in reverse order
    """
    my_list.reverse()
    for num in my_list:
        print('{}'.format(num))
