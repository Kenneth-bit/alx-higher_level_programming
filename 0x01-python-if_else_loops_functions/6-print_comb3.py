#!/usr/bin/python3
for number in range(0, 10):
    for digit in range(0, 10):
        if number < digit and (number + digit) != 17:
           print("{}{}".format(number, digit), end=', ')
        elif number < digit and (number + digit) == 17:
           print("{}{}".format(number, digit))
