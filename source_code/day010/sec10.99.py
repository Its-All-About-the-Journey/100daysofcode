def is_leap(year: int) -> bool:
    is_year_leap = False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_year_leap = True
        else:
            is_year_leap = True

    return is_year_leap

def days_in_month(year: int, month: int) -> int:
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    if (month >= 1) and (month <= 12):
        days = month_days[month - 1]
        
        if (month == 2) and is_leap(year):
            # Add one more day.
            days += 1
    else: # Out of range
        days = 0
    
    return days


  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)