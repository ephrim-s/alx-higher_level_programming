#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns weighted average of integers"""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    averg = 0
    size = 0
    for tple in my_list:
        averg += (tple[0] * tple[1])
        size += tple[1]
    return (averg / size)
