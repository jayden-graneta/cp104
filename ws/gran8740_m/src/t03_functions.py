"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: Jayden Graneta
ID:     169058740
Email:  gran8740@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants

# your constants here


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​‌​​​​‌‌​‌‌​‌​​:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    BASE = 125
    COST_PER_SERVICE = 25
    DISCOUNT = 0.10

    services = int(input('How many extra services are you purchasing?'))
    total_cost = BASE + (COST_PER_SERVICE * services)

    if services > 1:
        vip = input('Are you a VIP member (Y/N)?')
        if vip == 'Y':
            dis_amount = total_cost * DISCOUNT
            total_cost -= dis_amount
            return total_cost
        elif vip == 'N':
            return total_cost
        else:
            return total_cost
    return
