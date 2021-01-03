# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)
years_remaining = 90 - age_as_int
months_remaining = years_remaining * 12
weeks_remaining = months_remaining * 52
days_remaining = weeks_remaining * 365
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")