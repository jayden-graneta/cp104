"""
-------------------------------------------------------
[Compound interest Calculator ]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      1690587401
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-02"
-------------------------------------------------------
"""

prin = float(input('Principal: $'))
inter = float(input('Interest (%):'))
num_years = int(input('Number of years:'))
compound = int(input('Number of times interest compounded per year:'))

inter_rate = (inter / 1000) * num_years
money = prin * (1 + (inter_rate / compound))**(num_years * compound)

print("Balance: $", money)
