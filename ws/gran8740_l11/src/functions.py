"""
-------------------------------------------------------
[functions list]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports
import random
# Constants


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """

    matrix = []

    for x in range(rows):
        row = []
        for x in range(cols):
            if value_type == 'float':
                value = random.uniform(low, high)
            else:
                value = random.randint(int(low), int(high))
            row.append(value)
        matrix.append(row)

    return matrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    print("{:8}".format(""), end="")
    for col in range(num_cols):
        print("{:8}".format(col), end="")
    print()

    for row in range(num_rows):
        print("{:8}".format(row), end="")
        for col in range(num_cols):
            if value_type == 'float':
                print("{:8.2f}".format(matrix[row][col]), end="")
            else:
                print("{:8}".format(int(matrix[row][col])), end="")
        print()
    return


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
        Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = float('inf')
    largest = float('-inf')
    total = 0

    for row in matrix:
        for value in row:
            if value < smallest:
                smallest = value
            if value > largest:
                largest = value
            total += value

    num_elements = len(matrix) * len(matrix[0])
    average = total / num_elements

    return smallest, largest, total, average


def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            if value < n:
                loc = [row_index, col_index]

    return loc


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            matrix[row_index][col_index] = value * num
    return
