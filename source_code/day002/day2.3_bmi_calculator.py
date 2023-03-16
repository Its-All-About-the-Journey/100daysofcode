#BMI = weight / height**

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Set your equation and convert the variables to the correct type for performing math on them:
bmi = float(weight) / float(height) ** 2
#Print your results as an integer:
print(int(bmi))

#Alternitively you could round the bmi value so that the resulting integer BMI is more accurate:
print(round(bmi))