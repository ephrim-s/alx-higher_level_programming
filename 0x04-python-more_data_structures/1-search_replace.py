#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """searches and replaces all occurences"""
    list_1 = my_list[:]
    for x in range(len(list_1)):
        if list_1[x] == search:
            list_1[x] = replace
    return (list_1)
