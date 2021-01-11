"""
Day 010 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/10/2021
"""

# Functions with outputs

def format_name(f_name, l_name):
    """Takes input of a first name and last name and formats it to title case."""
    # Line above is a Docstring, place under the definition to dive user of function idea of what it does.
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("WaYNE", "KWIAT"))

# Ex 10.1 building on leap year function
def is_leap(leap_year_test):
    if leap_year_test % 4 == 0:
        if leap_year_test % 100 == 0:
            if leap_year_test % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(test_year, test_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and test_month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
