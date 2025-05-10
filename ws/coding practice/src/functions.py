"""
-------------------------------------------------------
[function list]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
from random import randint


def sum_even(num):
    sum = 0
    for i in range(2, num+1, 2):
        sum += i
    return sum


def sum_all(start, end, inc):
    total = 0
    for x in range(start, end+1, inc):
        total += x
    return total


def draw_rectangle(width, height, char):
    for i in range(width):
        print(char * height)
    return


def draw_triangle(base, char):
    for x in range(base+1):
        print(char * x)
    return


def draw_arrow(base, char):
    for x in range(base+1):
        print(char * x)
    for i in range(base-1, 0, -1):
        print(char * i)
    return


def statistics(n):
    user_input = float(input("First Value: "))

    max = user_input
    min = user_input
    total = user_input

    for x in range(n-1):
        user_in = float(input("Next Value: "))

        if user_in > max:
            max = user_in
        if user_in < min:
            min = user_in
        total += user_in
    average = total / n
    return min, max, total, average


def hi_lo_game(high):
    number = randint(1, high)
    count = 0
    guess = int(input('Guess:'))

    while guess != number:
        count += 1
        if guess > number:
            print('Too high, try again!')
            guess = int(input('Guess:'))
        else:
            print('Too low, try again!')
            guess = int(input('Guess:'))
    print('Congratulations - Good guess!')
    print(f'You made {count} guesses.')
    return count


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0

    while current < target:
        current *= (1 + rate / 100)
        years += 1
    return years


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    x = 0
    total = 0
    while total < (target+1):
        total += (x**2)
        x += 1
    return total


def positive_statistics():
    user_input = float(input('First positive value: '))

    max = user_input
    min = user_input
    total = user_input
    average = 0
    count = 0
    while user_input >= 0:
        user_input = float(input('Next positive value: '))

        if max < user_input:
            max = user_input
        if min > user_input and user_input > 0:
            min = user_input
        if user_input > 0:
            total += user_input
        count += 1
    average = total / count
    return min, max, total, average


def meal_costs():
    day = 1
    away = 'Y'
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0

    while away == 'Y':
        print(f'Day {day}')
        day += 1
        temp_total = 0

        breakfast = float(input('\nHow much was breakfast? $'))
        b_total += breakfast
        temp_total += breakfast

        lunch = float(input('How much was lunch? $'))
        l_total += lunch
        temp_total += lunch

        supper = float(input('How much was supper? $'))
        s_total += supper
        temp_total += supper
        print(f'Your total for the day was ${temp_total}')

        a_total += temp_total

        away = input('\nWere you away another day (Y/N)? $')
    return b_total, l_total, s_total, a_total


def get_weekday_name(d):
    days = ['Sunday', 'Monday', 'Tuesday',
            'Wednesday', 'Thursday', 'Friday']

    return days[d-1]


def generate_integer_list(n, low, high):
    number_list = []
    for x in range(n):
        number = randint(low, high)
        number_list.append(number)
    return number_list


def get_lotto_numbers(n, low, high):
    number_list = []
    for x in range(n):
        number = randint(low, high)
        number_list.append(number)
    number_list.sort()
    return number_list


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    smallest = min(values)
    largest = max(values)
    total = sum(values)
    average = total / len(values)

    return smallest, largest, total, average


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """

    negatives = 0
    positives = 0
    zeroes = 0
    evens = 0
    odds = 0

    for x in range(len(values)):
        if values[x] > 0:
            positives += 1
        elif values[x] < 0:
            negatives += 1
        else:
            zeroes += 1
        if values[x] % 2 == 0:
            evens += 1
        else:
            odds += 1
    return negatives, positives, zeroes, evens, odds


def linear_search(values, value):
    x = 0
    index = 0

    for x in range(len(values)):
        if value == values[x]:
            index = x
        else:
            x += 1
    return index


def dot_product(source1, source2):
    product = 0

    for x in range(len(source1)):
        product += (source1[x] * source2[x])
    return product


def symmetric_difference(source1, source2):
    target = []

    for item in source1:
        if item not in source2:
            target.append(item)
    for item in source2:
        if item not in source1:
            target.append(item)

    return target


def is_hydroxide(chemical):
    hydroxide = chemical.endswith('OH')

    return hydroxide


def parse_code(product_code):

    pc = product_code[0:3]
    pi = product_code[3:7]
    pq = product_code[7:]

    return pc, pi, pq


def validate_code(product_code):
    category = product_code[:3].isalpha() and product_code[:3].isupper()

    digits = product_code[3:7].isdigit()

    qualifiers = product_code[7:].startswith(
        tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    return category, digits, qualifiers


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """

    if len(password) < 8:
        print('not long enough')
    if not any(char.isdigit() for char in password):
        print("no digits")
    if not any(char.isupper() for char in password):
        print("no upper case")
    if not any(char.islower() for char in password):
        print("no lower case")
    return


def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    if s == s[::-1]:
        palindrome = True
    else:
        palindrome = False
    return palindrome


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    a = s.count('a')
    e = s.count('e')
    i = s.count('i')
    o = s.count('o')
    u = s.count('u')
    a_caps = s.count('A')
    e_caps = s.count('E')
    i_caps = s.count('I')
    o_caps = s.count('O')
    u_caps = s.count('U')

    lower_count = a + e + i + o + u
    upper_count = a_caps + e_caps + i_caps + o_caps + u_caps

    count = lower_count + upper_count
    return count


def total_digits(s):
    """
    Extracts and calculates the total of all digits in string.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    total = 0

    for char in s:
        if char.isdigit():
            total += int(char)

    return total


def customer_by_id(fh, id_number):
    """
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    fh.seek(0)

    # Initialize result to an empty list
    result = []

    # Read the first line from the file
    line = fh.readline().strip()

    # Use a while loop to search for the record with the given ID number
    while line:
        fields = line.split(',')
        if fields[0] == id_number:
            result = fields
            break  # Exit the loop if a match is found
        line = fh.readline().strip()

    return result
