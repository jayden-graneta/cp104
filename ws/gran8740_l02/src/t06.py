"""
-------------------------------------------------------
[Calculates the monthly mortgage rate using mortgage principal amount, number of monthly payments and, monthly interest rate.]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports

# Constants
MONTHS_IN_YEAR = 12

prin = float(input("Mortgage Principal ($): "))
years = int(input("Number of years: "))
num_month = years * MONTHS_IN_YEAR
inter = float(input("Yearly interest rate (%): "))

month_int = inter / 100 / MONTHS_IN_YEAR

payments = prin * ((month_int * (1 + month_int)**num_month) /
                   ((1 + month_int)**num_month - 1))

print("The monthly payments are: $", payments)
