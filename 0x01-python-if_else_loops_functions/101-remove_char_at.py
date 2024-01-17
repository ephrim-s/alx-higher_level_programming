#!/usr/bin/python3

def remove_chr_at(str, n):
    """create copy of str"""
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1])
