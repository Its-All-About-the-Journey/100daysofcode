# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 🚨 You have x days, y weeks, and z months left. 🚨
days = 365
weeks = 52
months = 12

result = 90 - int(age)
x = result * days
y = result * weeks
z = result * months
message = f"You have {x} days, {y} weeks, and {z} months left until your turn 90."
print(message)

# 🚨 1st Solution from exercise 🚨
# age_as_int = int(age)

# years_remaining = 90 - age_as_int
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} left until 90.")

# 🚨 2nd Solution from exercise 🚨
# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")