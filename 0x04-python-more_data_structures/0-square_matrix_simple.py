#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """calculates square value of integers of matrix"""
    return ([list(map(lambda i: i * i, row)) for row in matrix])
