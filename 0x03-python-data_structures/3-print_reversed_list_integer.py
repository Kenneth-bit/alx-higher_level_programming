#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ Prints the list elements in reverse order
    """
    if my_list is None:
        pass
    else:
        my_list.reverse()
        for item in my_list:
            if type(item) == int:
                try:
                    print("{:d}".format(item))
                except SyntaxError:
                    pass
            elif type(item) == str:
                try:
                    print("{:s}".format(item))
                except SyntaxError:
                    pass
