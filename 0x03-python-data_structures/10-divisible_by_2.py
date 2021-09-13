#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    validate = []
    for i in my_list:
        if i % 2 == 0:
            validate.append(True)
        else:
            validate.append(False)
    return validate
