"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740  
Email:   gran8740@mylaurier.ca
__updated__ = "2023-12-13"
-------------------------------------------------------
"""
# Imports
from functions import population_growth
from functions import sum_squares
from functions import positive_statistics
from functions import meal_costs
from functions import get_weekday_name
from functions import generate_integer_list
from functions import get_lotto_numbers
from functions import list_stats
from functions import list_categorize
from functions import linear_search
from functions import dot_product
from functions import symmetric_difference
# Constants

print(population_growth(10000, 1000, 10))
print(sum_squares(9))
# print(positive_statistics())
# print(meal_costs())
print(get_weekday_name(2))
print(generate_integer_list(6, 1, 100))
print(get_lotto_numbers(8, 1, 99))
print(list_stats([94, 96, -22, -79, -28, -26, -50, 71, 24, -32]))
print(list_categorize([94, 96, -22, -79, -28, -26, -50, 71, 24, -32]))
print(linear_search([94, 96, -22, -79, -28, -26, -50, 71, 24, -32], -22))
print(dot_product([10.0, 3.0, 10.0, 3.0, 1.0], [8.0, 2.0, 7.0, 3.0, 6.0]))
print(symmetric_difference([10, 3, 10, 3, 1], [8, 2, 7, 3, 6, 10, 32, 99]))
