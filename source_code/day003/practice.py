# 3.1 - Even or odd
# ---------------------------------------------------------
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

print(f"This is an {'odd' if number % 2 else 'even'} number")


# 3.2 - bmi calc 2.0
# ---------------------------------------------------------
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# from bmi 1.0
bmi = round(float(weight) / (float(height) ** 2))

print(f"Your BMI is {bmi}, ", end="")

if bmi < 18.5:
  print("you are underweight.")
elif bmi < 25:
  print("you have a normal weight.")
elif bmi < 30:
  print("you are slightly overweight.")
elif bmi < 35:
  print("you are obese.")
else:
  print("you are clinically obese.")