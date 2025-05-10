"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740  
Email:   gran8740@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from functions2 import customer_record
from functions import customer_by_id
# Constants

fh = open("customers.txt", "r", encoding="utf-8")

print(customer_record(fh, 3))
print(customer_by_id(fh, 23456))
