"""
-------------------------------------------------------
[Formatting print statments with underscores]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-09-26"
-------------------------------------------------------
"""

first = 100
second = 34
third = 933

total = first + second + third

print("Values")
print(f'First:  {first:_>6d}')
print(f'Second: {second:_>6d}')
print(f'Third:  {third:_>6d}')
print(f'Total:  {total:_>6d}')
