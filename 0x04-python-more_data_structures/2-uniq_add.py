#!/usr/bin/python3

def uniq_add(my_list=[]):
    """sum up all uniqe integers in list"""
    sum = 0
    for i in set(my_list):
        sum += i
    return (sum)
