#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print integers in reverse"""
    if isinstance(my_list, list):
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))
