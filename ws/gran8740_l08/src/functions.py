"""
-------------------------------------------------------
[Functions]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-11-10"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    i = 0
    while i < n:
        values.append(randint(low, high))
        i += 1
    return values


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odd = 0
    length = len(values)
    n = 0

    while n < length:
        if values[n] < 0:
            negatives += 1
        elif values[n] > 0:
            positives += 1
        else:
            zeroes += 1

        if values[n] % 2 == 0:
            evens += 1
        else:
            odd += 1
        n += 1
    return negatives, positives, zeroes, evens, odd


def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """

    length = len(values)
    n = 0
    indexes = []

    while n < length:
        if values[n] == value:
            indexes.append(n)
        n += 1
    return indexes


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the union of source1 and source2 (list of *)
    -------------------------------------------------------
    """
    target = []
    i = 0

    while i < len(source1):
        if source1[i] not in target:
            target.append(source1[i])
        i += 1

    i = 0

    while i < len(source2):
        if source2[i] not in target:
            target.append(source2[i])
        i += 1

    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2, but not both,
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the symmetric difference of source1 and source2 (list of *)
    -------------------------------------------------------
    """

    target = []
    i = 0

    while i < len(source1):
        if source1[i] not in source2 and source1[i] not in target:
            target.append(source1[i])
        i += 1

    i = 0

    while i < len(source2):
        if source2[i] not in source1 and source2[i] not in target:
            target.append(source2[i])
        i += 1

    return target
