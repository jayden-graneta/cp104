"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740  
Email:   gran8740@mylaurier.ca
__updated__ = "2024-01-07"
-------------------------------------------------------
"""
# Imports
from pokedex import starter
# Constants

print('Hello Trainer! Welcome to the start of your pokemon journey!!')
print('\nPlease select one of the following starter Pokemon:')
print("------------------------")
for pokemon in starter: 
    print(f"Pokemon Name: {pokemon[0]}")
    print(f"Type: {pokemon[1]}")
    print(f"Moves: {', '.join(pokemon[2:])}")
    print("------------------------")
partner = input()

print(f'\nCongrats! You selected {partner} as your Pokemon partner')
