"""
-------------------------------------------------------
[Formatting print statements and finding the total of three values]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-09-26"
-------------------------------------------------------
"""

dirt = float(input("Enter amount of dirt (m^3):"))
gravel = float(input("Enter amount of gravel (m^3):"))
sand = float(input("Enter amount of sand (m^3):"))

total = dirt + gravel + sand

print()
print("Material   Cubic Metres")
print(f"Dirt       {dirt:5.1f}")
print(f'Gravel     {gravel:5.1f}')
print(f'Sand       {sand:5.1f}')
print(f'Total      {total:5.1f}')
