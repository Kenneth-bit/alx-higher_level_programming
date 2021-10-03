#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) < 123:
           cap_str = chr(ord(char) - 32)
        else:
           cap_str = char
        print("{}".format(cap_str), end='')
    print()
