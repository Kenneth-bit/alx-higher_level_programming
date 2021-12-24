#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_elem = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            num_elem += 1
        except (ValueError, TypeError):
            pass
    print("")
    return num_elem
