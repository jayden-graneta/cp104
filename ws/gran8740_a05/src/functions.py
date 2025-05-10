"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-11-04"
-------------------------------------------------------
"""
# Imports

# Constants


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """

    if number == 0:
        product = 1
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


def calories_treadmill(per_min, minutes):
    """
    Parameters:
        per_min - Calories burned per minute (float)
        minutes - Total number of minutes run (int)
    Returns:
        None
    """
    print(f"{'Time':<4} {'Calories Burned':<5}")
    for time in range(5, minutes + 1, 5):
        calories = per_min * time
        print(f"{time:<4} {calories:<5.1f}")
    return None


def arrow_up(rows):
    """
    Prints an arrow pointing upwards with a specified number of rows.
    Use: arrow_up(rows)
    Parameters:
        rows - The number of rows in the arrow (int)

    Returns:
        None
    """
    for i in range(0, rows, 1):
        if (i == 0):
            pattern = (" "*(rows-(i+1)) + "#")
        else:
            pattern = (((" "*(rows-(i+1))) + "#" + (" "*(2*i-1)) + "#"))
        print(pattern)

    return None


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    print(" "*4, end="")
    for i in range(start_num, stop_num+1, 1):
        print(f"{i:4} |", end="")
    print()
    print((" "*4) + "-"*((stop_num-start_num)*4+4))

    for i in range(start_num, stop_num+1, 1):
        print(f"{i:2} |", end="")
    for a in range(start_num, stop_num+1, 1):
        number = i*a
        print(f"{number:4}", end="")
        print("")

    return None


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
    """

    total = 0
    for i in range(start, start+(increment*count), increment):
        total += i

    return total
