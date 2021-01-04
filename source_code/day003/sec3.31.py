# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

NORMAL_YEAR_DAYS = 365
LEAP_YEAR_DAYS   = NORMAL_YEAR_DAYS + 1


# Leap year truth table
# Evenly divisible by 4
# ----------------------------------
# 4 | 100 | 400 | Is it a leap year?
# ----------------------------------
# T |  T  |  T  | YES
# T |  T  |  F  | NO
# T |  F  |  T  | YES
# T |  F  |  F  | YES 
# F |  T  |  T  | NO
# F |  T  |  F  | NO
# F |  F  |  T  | NO
# F |  F  |  F  | NO
# ^----^---------------- If T F X, always a leap year
# ^----^-----^---------- If T T T, always a leap year
# ---------------------- Others, always not a leap year

year_4   = not bool(year % 4)
year_100 = not bool(year % 100)
year_400 = not bool(year % 400)

if ( year_4 & ~year_100 ) or ( year_4 & year_100 & year_400 ):
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')