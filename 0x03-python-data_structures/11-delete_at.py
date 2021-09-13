#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return my_list
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    value = my_list[idx]
    my_list.remove(value)
    lists = my_list
    return lists
