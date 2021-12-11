#!/usr/bin/python3
def search_replace(my_list, search, replace):
	''' search_replace --  replaces all occurrences of an element by another in a new list.
	    new_list -- modified list.
	    my_list -- input list.
	    search -- element to be replaced.
	    replace -- element to be inserted.
        '''
    new_list = my_list.copy()
    for number in range(len(my_list)):
        if new_list[number] == search:
            new_list[number] = replace
    return new_list
