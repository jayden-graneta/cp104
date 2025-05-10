"""
-------------------------------------------------------
[count word frequency]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-11-24"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word
# Constants

fh = open("words.txt", 'r')

print(count_frequency_word(fh, 'Python'))
