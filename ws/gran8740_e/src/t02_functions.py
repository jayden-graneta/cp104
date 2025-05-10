"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Constants

# Your constants here


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """

    dry_days = 0
    damp_days = 0
    wet_days = 0
    avg = 0

    DRY = 4
    DAMP = 8

    user_input = int(input('Rainfall mm (-1 to stop): '))

    while user_input >= 0:
        if user_input < DRY:
            dry_days += 1
            avg += user_input
        elif user_input >= DRY and user_input < DAMP:
            damp_days += 1
            avg += user_input
        else:
            wet_days += 1
            avg += user_input
        user_input = int(input('Rainfall mm (-1 to stop): '))
    total_days = wet_days + dry_days + damp_days
    avg /= total_days

    '''
    print(f'Dry days: {dry_days}')
    print(f'Damp days {damp_days}')
    print(f'Wet days {wet_days}')
    print(f'Average rainfall (mm) {avg}')
    '''

    return dry_days, damp_days, wet_days, avg
