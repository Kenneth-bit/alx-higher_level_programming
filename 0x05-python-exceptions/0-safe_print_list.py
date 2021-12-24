#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num_elem = 0
        for num in range(x):
            print(my_list[num], end="")
            num_elem += 1
        print("")
    except IndexError:
        print("")

    return num_elem
