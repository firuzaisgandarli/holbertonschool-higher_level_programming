#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared"""
    return [[x * x for x in row] for row in matrix]
