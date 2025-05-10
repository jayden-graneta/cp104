"""
-------------------------------------------------------
[functions list]
-------------------------------------------------------
Author:  Jayden Rey Graneta
ID:      169058740
Email:   gran8740@mylaurier.ca
__updated__ = "2023-10-27"
-------------------------------------------------------
"""
# Imports


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0

    for x in range(start, finish + 1, increment):
        total += x
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for x in range(1, height + 1):
        spaces = ' ' * (height - x)
        print(spaces + char * (2 * x - 1))
    return


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_arrow(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in range(1, width + 1):
        print(char * i)
    for i in range(width - 1, 0, -1):
        print(char * i)
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    print("Year       Value $")
    print("------------------")

    for year in range(years + 1):
        print(f"{year:2}      {value:,.2f}")
        if year != years:
            value = value * (1 + rate / 100)
    return value


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """

    GRAVITY = 9.8
    total_hours = 0

    for week in range(1, 7):
        print(f"Week {week}")
        for ia in range(1, ia_count + 1):
            hours = float(input(f"  Marking hours for IA {ia}: "))
            total_hours += hours
    print(f"{total_hours:.2f}")
    return total_hours
