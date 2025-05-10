"""
-------------------------------------------------------
[line numbering]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import line_numbering
# Constants
input_file_path = "wilde.txt"
output_file_path = "wilde_numbered.txt"

with open(input_file_path, "r", encoding="utf-8") as fh_read, open(output_file_path, "w", encoding="utf-8") as fh_write:
    line_numbering(fh_read, fh_write)
