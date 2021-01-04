# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

name1_true = lower_name1.count('t') + lower_name1.count('r') + lower_name1.count('u') + lower_name1.count('e')

name1_love = lower_name1.count('l') + lower_name1.count('o') + lower_name1.count('v') + lower_name1.count('e')

name2_true = lower_name2.count('t') + lower_name2.count('r') + lower_name2.count('u') + lower_name2.count('e')

name2_love = lower_name2.count('l') + lower_name2.count('o') + lower_name2.count('v') + lower_name2.count('e')

total_true = name1_true + name2_true
total_love = name1_love + name2_love

love_score = (total_true * 10) + total_love 

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
  print(f"Your love score is {love_score}, you are alright together.")
else:
  print(f"Your love score is {love_score}")