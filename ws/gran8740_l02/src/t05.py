"""
-------------------------------------------------------
[Calculates total pay for the week bu the hourly rate and hours worked.]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""
# Imports

# Constants
hour_rate = float(input("Hourly rate of pay:"))
hour_work = float(input("Hours worked for the week:"))
total_pay = hour_rate * hour_work

print("Total pay for the week: $", total_pay)
