#!/usr/bin/python3
"""This module defines a function matrix_mul() that multiplies two
matrix, in order for the matrix to be valid for multiplication
the rows of the first matrix should be equals to the columns of
the second matrix"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
        m_a (list): A list of lists representing the first matrix.
        m_b (list): A list of lists representing the second matrix.

    Returns:
        list: A list of lists representing the result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
        ValueError: If m_a or m_b is empty or if they cannot be multiplied.
        TypeError: If m_a contains elements that are not integers or floats.
        TypeError: If m_b contains elements that are not integers or floats.

    """

    # Validate m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate m_a and m_b are not empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Validate m_a contains only integers or floats
    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    # Validate m_b contains only integers or floats
    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # Validate m_a and m_b are rectangles (all rows should be of the same size)
    a_row_size = len(m_a[0])
    b_row_size = len(m_b[0])
    if any(len(row) != a_row_size for row in m_a):
        raise TypeError("Each row of m_a must be of the same size")
    if any(len(row) != b_row_size for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Validate if m_a and m_b can be multiplied
    if a_row_size != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(element)
        result.append(row)

    return result
