# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#This is how you work out whether if a particular year is a leap year.

#on every year that is evenly divisible by 4 
#**except** every year that is evenly divisible by 100 
#**unless** the year is also evenly divisible by 400

by4 = year % 4
by100 = year % 100
by400 = year % 400

if by4 != 0:
  print("Not leap year.")
elif by400 != 0 and by100 == 0:
  print("Not leap year.")
else:
  print("Leap Year.")
  
# Could also be solved with nest if:
#
#if by4 != 0:
#  print("Not leap year.")
#elif by100 == 0:
#  if by400 != 0:
#    print("Not leap year.")
#  else:
#    print("Leap year.")
#else:
#  print("Leap year.")