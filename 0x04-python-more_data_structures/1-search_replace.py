#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for number in range(1, len(my_list) + 1):
        if number == search:
            new_list.insert(search, replace)
        else:
            new_list.append(number)
    return new_list
