"""
-------------------------------------------------------
[PROJECTED TAX REPORT]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

total_sales = float(input('Enter the total sales:'))
ANNUAL_TAX = 18.50
tax = total_sales * (ANNUAL_TAX * 0.01)

print('Projected Tax Report')
print('--------------------------')
print('Total sales:     $', total_sales)
print('Annual tax:      %', ANNUAL_TAX)
print('--------------------------')
print('Tax:             $', tax)
