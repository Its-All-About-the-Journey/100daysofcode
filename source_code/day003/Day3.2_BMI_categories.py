# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
underweight = f"Your BMI is {bmi}, you are underweight!"
normalweight = f"Your BMI is {bmi}, you have a normal weight."
overweight = f"Your BMI is {bmi}, you are slightly overweight."
obese = f"Your BMI is {bmi}, you are obese!"
clinicobese = f"Your BMI is {bmi}, you are clinically obese!"
print(bmi)

if bmi <= 18.5:
    print(underweight)
elif bmi < 25:
    print(normalweight)
elif bmi < 30:
    print(overweight)
elif bmi < 35:
    print(obese)
else:
    print(clinicobese)
