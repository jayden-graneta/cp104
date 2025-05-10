"""
-------------------------------------------------------
[functions]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports

# Constants


def list_factors(number):
    """
    -------------------------------------------------------
    Returns a list of all the factors for a given number 
    Use: factors = list_factors(number)
    -------------------------------------------------------
    Parameters:
        number - The integer greater than 0 for which factors need to be determined. (int)
    Returns:
        list - A list of factors of the input number.
    ------------------------------------------------------
    """
    factors = []

    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    positives = []
    number = int(input('Enter a positive number:'))

    while number >= 1 or number <= -1:
        if number > 0:
            positives.append(number)
            number = int(input('Enter a positive number:'))
        else:
            number = int(input('Enter a positive number:'))
    return positives


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """

    index_list = []

    for i in range(len(numbers)):
        if numbers[i] == target_number:
            index_list.append(i)

    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for value in subtrahend:
        indexes = get_indexes(minuend, value)
        for index in reversed(indexes):
            minuend.pop(index)
    return


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            in_order = False
            index = i + 1
            break

    return in_order, index
