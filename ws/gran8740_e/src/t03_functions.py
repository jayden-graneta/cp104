"""
-------------------------------------------------------
Exam Task 3 Function Definitions
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""


def upper_vowels(string):
    """
    -------------------------------------------------------
    Converts vowels in a string to upper-case, all other 
    letters to lower-case. Non letters are left unchanged.
    Vowels include: aeiou.
    Use: altered = upper_vowels(string)
    -------------------------------------------------------
    Parameters:
        string - string to process (str)
    Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
        altered - the resulting string (str)
    -------------------------------------------------------
    """

    altered = ''

    for x in range(len(string)):
        if string[x] == 'a' or string[x] == 'e':
            altered += string[x].upper()
        elif string[x] == 'i' or string[x] == 'o':
            altered += string[x].upper()
        elif string[x] == 'u':
            altered += string[x].upper()
        else:
            altered += string[x].lower()

    return altered
