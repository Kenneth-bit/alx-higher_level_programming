#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    j = 1
    for i in my_list:
        if j == search:
            new_list.insert(search, replace)
        else:
            new_list.append(i)
        j += 1
    return new_list
