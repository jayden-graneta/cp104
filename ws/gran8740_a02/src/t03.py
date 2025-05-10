"""
-------------------------------------------------------
[DATE FORMATTER]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants

raw_date = int(input('Enter a date in the format YYYYMMDD:'))

year = raw_date // 10000
month = raw_date // 100 % 100
day = raw_date % 1000

print(f'The reformatted date: {year}/{month}/{day}')
