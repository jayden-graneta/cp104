"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740  
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants
num_flyers = int(input('Number of flyers:'))
num_people = int(input('Number of delivery people:'))

flyers_people = num_flyers // num_people
flyers_left = num_flyers % num_people

print('Flyers per delivery person:', flyers_people)
print('Flyers left over:', flyers_left)
