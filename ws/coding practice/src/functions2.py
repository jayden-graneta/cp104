"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740  
Email:   gran8740@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports

# Constants

special = '1357 Country Ln.'
s_string = special[:4]
print(s_string)

mystr = 'yes'
yourstr = 'no'
mystr += yourstr * 2
print(mystr)

my_string = '03/07/2018'
list_strip = my_string.split('/')
print(list_strip)

total1 = 1500
total2 = 2500
if (total1 + total2 != 5000):
    if (total2 - total1 == 1000 and total1 > 2000):
        print("First")
    elif (total2 - total1 > 1000):
        print("Second")
    else:
        print("Third")
else:
    if (total2 != 2500):
        print("Fourth")
    else:
        print("Fifth")


a = 3
b = 10
c = 24
result = (b != c) and (not b <= c)
print(result)

total = 0
stop = 5

for i in range(stop):
    total = total + i
    i = i + stop
print(total)
