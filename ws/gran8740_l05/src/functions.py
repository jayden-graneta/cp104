"""
-------------------------------------------------------
[List of functions]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-20"
-------------------------------------------------------
"""
# Imports

# Constants


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    GRAVITY = 9.8
    weight = mass * GRAVITY

    if weight > 1000:
        message = 'heavy'
    elif weight < 10:
        message = 'light'
    else:
        message = 'average'

    return weight, message


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """

    if year % 4 == 0:
        result = True
        if year % 100 == 0:
            result = False
            if year % 400 == 0:
                result = True
            else:
                result = False
        else:
            result = False
    else:
        result = False
    return result


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """

    if speed < 0:
        category = "Unknown"
    elif speed < 39:
        category = "Breeze"
    elif 39 <= speed <= 61:
        category = "Strong Wind"
    elif 62 <= speed <= 88:
        category = "Gale Winds"
    elif 89 <= speed <= 117:
        category = "Whole Gale"
    elif 89 <= speed <= 117:
        category = "Whole Gale"
    else:
        category = "Hurricane"
    return category


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """

    if x == 0 and y == 0:
        location = 'Origin'
    elif x != 0 and y == 0:
        location = 'X-Axis'
    elif x == 0 and y != 0:
        location = 'Y-Axis'
    elif x > 0 and y > 0:
        location = 'Quadrant 1'
    elif x < 0 and y > 0:
        location = 'Quadrant 2'
    elif x < 0 and y < 0:
        location = 'Quadrant 3'
    else:
        location = 'Quadrant 4'
    return location


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    age = int(input('How old are you?'))

    ADULT = 18
    SENIOR = 65
    STUDENT = 10
    KID = 3

    if age >= SENIOR:
        price = 4.0
    elif age >= ADULT:
        price = 5.0
    elif age >= KID and age < STUDENT:
        price = 2.0
    elif age >= STUDENT and age < ADULT:
        student = input('Are you a student at this school: Y/N')
        if student == 'Y':
            price = 1.0
        elif student == 'N':
            price = 3.0
    else:
        price = 0
    return price
