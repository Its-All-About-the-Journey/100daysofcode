# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

numerator = float(weight)
denominator = float(height) ** 2

BMI = int( numerator / denominator )

print( BMI )

# Height: 1.8 m
# Weight: 99.3 kg
# BMI: 30.65
# I am obese.  2021 Goals --> Normal LMAO

# https://maniacs.info/body-mass-index/is-a-bmi-of-30.65-good.html
# Underweight: 18.49 and less
# Normal: 18.50 to 24.99
# Overweight: 25.00 to 29.99
# Obese: 30 or greater