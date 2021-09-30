#!/usr/bin/python3
for num in range(0, 10):
    for dgt in range(0, 10):
        if num < dgt and (num + dgt) != 17:
            print("{}{}".format(num, dgt), end=', ')
        elif num < dgt and (num + dgt) == 17:
            print("{}{}".format(num, dgt))
