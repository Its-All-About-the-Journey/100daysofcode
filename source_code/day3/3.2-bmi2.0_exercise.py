# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

# Hint
# Try to use the exponent ** operator in your code.
# Remember to round your result to the nearest whole number.
# Make sure you include the words in bold from the interpretations.

#Write your code below this line 👇
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, You are in the normal weight range")
elif bmi < 30:
    print(f"Your BMI is {bmi}, You are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, You are obese")
elif bmi > 35:
    print(f"Your BMI is {bmi}, You are clinically obese")
else:
    print("You have entered incorrect information")