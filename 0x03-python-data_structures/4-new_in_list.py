#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	"""Replace number in duplicate list
	"""
	if idx < 0 or len(my_list) - 1 < idx:
	    return my_list

	list_two = my_list.copy()
	list_two[idx] = element
	return list_two
