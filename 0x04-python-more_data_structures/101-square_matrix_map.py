#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """computes the square value of integers"""
    return (list(map(lambda i: list(map(lambda j: j ** 2, i[:])), matrix)))
