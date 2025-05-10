"""
-------------------------------------------------------
[calculates the flyers given per volunteer and the leftover amount]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports

num_flyers = int(input("Number of flyers:"))
num_vol = int(input("Number of volunteers:"))

flyer_per = num_flyers // num_vol
leftover = num_flyers % num_vol

print("Flyers per volunteer:", flyer_per)
print("Flyers leftover:", leftover)
