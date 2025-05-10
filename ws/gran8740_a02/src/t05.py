"""
-------------------------------------------------------
[BRICK AND CONCRETE COST CALCULATOR]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-07"
-------------------------------------------------------
"""
# Imports

# Constants
length = float(input('Foundation length (m):'))
width = float(input('Foundation width (m):'))
height = float(input('Foundation height (m):'))
wall_h = float(input('Wall height (m):'))
conc_cost = float(input('Cost of concrete ($/m^2):'))
brick_cost = float(input('Cost of bricks ($/m^2):'))

conc_needed = length * width * height
conc_price = conc_needed * conc_cost
brick_needed = (length * wall_h * 2) + (width * wall_h * 2)
brick_price = brick_needed * brick_cost
total_cost = brick_price + conc_price

print()
print(f'Concrete needed for foundation (m^3): {conc_needed:,.2f}')
print(f'Cost of concrete: ${conc_price:,.2f}')
print(f'Bricks needed for walls (m^2): {brick_needed:,.2f}')
print(f'Cost of bricks: ${brick_price:,.2f}')
print(f'Total cost: ${total_cost:,.2f}')
