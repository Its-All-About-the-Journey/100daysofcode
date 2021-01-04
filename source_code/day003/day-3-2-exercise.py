# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# bmi = round(((float(weight)) / (float(height) ** 2)), 2)
# print ("your BMI is " + str(int(bmi)))
bmi = 18
if bmi < 18.5:
  print ("your BMI is " + str(float(bmi)) + " and you are underweight")
elif 18.5 <= bmi <= 25:
  print ("your BMI is " + str(float(bmi)) + " and you have a normal weight")
elif 25 <= bmi <= 30:
  print ("your BMI is " + str(float(bmi)) + " and you are slightly overweight")
elif 30 <= bmi <= 35:
  print ("your BMI is " + str(float(bmi)) + " and you are obese")
elif 35 <= bmi:
  print ("your BMI is " + str(float(bmi)) + " and you are clinically obese")