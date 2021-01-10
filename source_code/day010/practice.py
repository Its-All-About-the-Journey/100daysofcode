# 10.1
# ---------------------------------------------------
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Take a year and month number, and return the numbers of days"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = month_days[month - 1]
    if month == 2 and is_leap(year):
        days += 1
    return days


#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)