#!/usr/bin/python3
def print_list_integer(my_list=[]):
	""" This functions prints all\
		integers in a list

	    Return : Integers in the list, one per line.
	"""
	for num in my_list:
	    print('{:d}'.format((num)))
