# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Convert age to an integer
age = int(age)
#Calculate the number of days and assign to a variable:
num_days = 90*365 - age*365
#Calculate the number of weeks and assign to a variable:
num_weeks = 90*52 - age*52
#Calculate the number of months and assign to a variable:
num_months = 90*12 - age*12
#Print the results using an f-string:
print(f"You have {num_days} days, {num_weeks} weeks, and {num_months} months left.")