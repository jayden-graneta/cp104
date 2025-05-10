"""
-------------------------------------------------------
[file copy]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import file_copy
# Constants

fh_1 = open("words.txt", 'r')

fh_2 = open("new_words.txt", 'w')
file_copy(fh_1, fh_2)

print(fh_2)
