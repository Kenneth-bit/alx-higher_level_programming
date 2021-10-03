#!/usr/bin/python3
def print_last_digit(number):
	if number < 0:
	    num = number * -1
	    last_digit = num % 10
	else:
	    num = number
	    last_digit = num % 10
	print("{}".format(last_digit), end='')
	return last_digit
