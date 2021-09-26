#!/usr/bin/python3
for number in range(0, 100):
    if number < 10 and number != 99:
        print("0{}".format(number), end=', ')
    elif number != 99:
        print("{}".format(number), end=', ')
    else:
        print("{}".format(number))
