#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
	"""Prints the list elements in reverse order
	"""
	for num in range(1, (len(my_list) + 1)):
		print(str.format(str(my_list[-num])))
