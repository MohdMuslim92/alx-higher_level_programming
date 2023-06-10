#!/usr/bin/python3
"""This module createsva function that divide a matrix
by a number"""


def matrix_divided(matrix, div):
    """Function that divides every element in a matrix by a divisor"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                "of integers/floats")

    row_lengths = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                    "of integers/floats")
        row_lengths.append(len(row))

    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
            new_element = round(element / div, 2)
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
