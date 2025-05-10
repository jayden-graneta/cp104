"""
-------------------------------------------------------
[Calculates the cost of a meal with tax and tip included]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-09-21"
-------------------------------------------------------
"""

subtotal = float(input("Food Charge:"))
tax = float(input("Sales tax in (%):"))
tip = float(input("Tip in (%):"))

sales_tax = subtotal * (tax * 0.010)
total_tip = subtotal * (tip * 0.010)
total = subtotal + total_tip + sales_tax

print("Cost of meal:")
print("Subtotal:", subtotal)
print("     Tax:", sales_tax)
print("     Tip:", total_tip)
print("-----------------------")
print("    Total:", total)
