"""
-------------------------------------------------------
Midterm B Task 2 Testing
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Imports
from t02_functions import categorize

strokes = int(input("Enter strokes: "))
rating = categorize(strokes)
print(f"categorize({strokes}) -> {rating}")
