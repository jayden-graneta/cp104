"""
-------------------------------------------------------
[functions]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports

# Constants


def total_wins():
    """
    -------------------------------------------------------
    Counts the number of wins for the "purple" and "gold" teams.

    Use: 
    -------------------------------------------------------
    Parameters:
        winner - Represents the winning team entered by the user (str)
    Returns:
        purp_wins - Represents the amount of purple wins (int)
        gold_wins - Represents the amount of gold wins (int)
    ------------------------------------------------------
    """

    purp_wins = 0
    gold_wins = 0
    winner = input('Enter the winning team:')

    while winner != '':
        if winner == 'purple':
            purp_wins += 1
            winner = input('Enter the winning team:')
        elif winner == 'gold':
            gold_wins += 1
            winner = input('Enter the winning team:')
        else:
            winner = input('Enter the winning team:')
    return purp_wins, gold_wins


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    prime = False
    i = 2

    if number == 1:
        prime = False

    elif number > 1:
        while prime == False:
            if number % i == 0:
                if number == i:
                    prime = True
                    break
                else:
                    prime = False
                    break
            else:
                i += 1
    return prime


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month   Interest   Payment   Balance")
    print("----------------------------------")

    month = 1
    balance = principal_amount

    while balance > 0:
        interest = (interest_rate / 100) * (balance / 12)
        balance = balance - (payment - interest)

        balance = max(balance, 0)

        print(f"{month:4}   {interest:8.2f}   {payment:8.2f}   {balance:8.2f}")
        month += 1
    return None


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    if number < 0:
        number = abs(number)

    digits = 0

    while number > 0:
        number //= 10
        digits += 1

    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    divisor = 1

    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1

    return total
