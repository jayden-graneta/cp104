"""
-------------------------------------------------------
[functions]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """

    number = randint(1, high)

    guess = 0
    count = 0

    while guess != number:
        guess = int(input("Guess:"))
        count += 1
        if guess < number:
            print("Too low, try again")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations - good guess!")
    print(f'You made {count} guesses')
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1
    while power < target:
        power *= 2
    return power


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    minimum = 0.0
    maximum = 0.0
    total = 0.0
    count = 0.0

    number = float(input("First positive number : "))

    while number >= 0:
        number = float(input("Next positive number : "))

        if number < minimum and number >= 0:
            minimum = number
        if number > maximum and number >= 0:
            maximum = number

        if number >= 0:
            total += number
            count += 1

        if count > 0:
            average = total / count
        else:
            average = 0.0
    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """

    expense = float(input('Enter an expense (0 to quit): $'))
    expenses = expense
    balance = available - expense

    while expense > 0:
        expense = float(input('Enter another expense (0 to quit): $'))

        expenses += expense
        balance -= expense

        if balance > 0:
            status = 'Surplus'
        elif balance < 0:
            status = 'Deficit'
        else:
            status = 'Balanced'
    return expenses, balance, status


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    total = 0.0
    count = 0
    TAX_RATE = 3.625 / 100
    OVERTIME = 40
    OVERTIME_RATE = 1.5

    while True:
        employee_id = int(input("Employee ID: "))
        if employee_id == 0:
            break
        hourly_wage_rate = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))
        if hours_worked > OVERTIME:
            overtime_hours = hours_worked - OVERTIME
            gross_payment = OVERTIME * hourly_wage_rate + \
                overtime_hours * (1.5 * hourly_wage_rate)
        else:
            gross_payment = hours_worked * hourly_wage_rate
        tax_deduction = gross_payment * TAX_RATE
        net_payment = gross_payment - tax_deduction
        total += net_payment
        count += 1
    if count == 0:
        average = 0.0
    else:
        average = total / count

    return total, average
