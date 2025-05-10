"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports

# your imports here
from t07_functions import line_lengths
# Your code here

fh = open('source.txt', "r+", encoding="utf-8")
f_short = open('fshort.txt', 'w+', encoding='utf-8')
f_long = open('f_long.txt', 'w+', encoding='utf-8')

print(line_lengths(fh, f_short, f_long, 5))

fh.close()
f_short.close()
f_long.close()
