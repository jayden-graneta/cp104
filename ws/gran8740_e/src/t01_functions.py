"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """
    count = 0
    ea = 0

    for x in range(len(values)):
        if values[x] == 0:
            count += 0
        elif values[x] % 2 == 0:
            ea += values[x]
            count += 1

        if ea != 0:
            ea /= count
    return ea
