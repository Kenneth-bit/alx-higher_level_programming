#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for number in range(len(my_list)):
        if new_list[number] == search:
            new_list[number] = replace
    return new_list



#def search_replace(my_list, search, replace):
#    def s_r_elm(elm):
#        return (elm if elm != search else replace)
#    return list(map(s_r_elm, my_list))
