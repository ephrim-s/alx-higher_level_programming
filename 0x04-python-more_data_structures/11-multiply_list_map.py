#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """returns list with all values multiplied by num"""
    return (list(map(lambda i: i*number, my_list)))
