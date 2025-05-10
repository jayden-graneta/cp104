"""
-------------------------------------------------------
[THE DIFFRENCE OF DIGITS FROM A TWO DIGIT NUMBER12]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants

num = int(input('Enter a positive digit number:'))

first = num % 10
sec = num // 10
diff = sec - first

print("The difference of the digits of", num, 'is', diff)
