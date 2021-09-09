#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    _sum = add(a, b)
    prod = mul(a, b)
    quot = div(a, b)
    diff = sub(a, b)
    print("{} + {} = {}".format(a, b, _sum))
    print("{} + {} = {}".format(a, b, diff))
    print("{} + {} = {}".format(a, b, prod))
    print("{} + {} = {}".format(a, b, div))
