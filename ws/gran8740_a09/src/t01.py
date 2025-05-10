"""
-------------------------------------------------------
[file top]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import file_top
# Constants

file_handle = open("students.txt", "r", encoding="utf-8")
file_top(file_handle, 5)
