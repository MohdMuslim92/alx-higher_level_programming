#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_list = []
    square_list = [[element * element for element in row] for row in matrix]
    return square_list
