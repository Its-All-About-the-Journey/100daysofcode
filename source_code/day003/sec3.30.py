# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# Messages - {} is for BMI value
BMI_CLINICALLY_OBESE_MSG = 'Your BMI is {}, you are clinically obese'
BMI_OBESE_MSG            = 'Your BMI is {}, you are obese'
BMI_OVERWEIGHT_MSG       = 'Your BMI is {}, you are slightly overweight'
BMI_NORMAL_MSG           = 'Your BMI is {}, you have a normal weight'
BMI_UNDERWEIGHT_MSG      = 'Your BMI is {}, you are underweight'

# BMI threshold
BMI_CLINICALLY_OBESE = 35       #                    bmi >= 35
BMI_OBESE            = 30       # clinically obese > bmi > 30
BMI_OVERWEIGHT       = 25       # obese            > bmi > 25
BMI_NORMAL           = 18.5     # overweight       > bmi > 18.5
# BMI_UNDERWEIGHT               # normal           > bmi

# BMI calculation
bmi = round( weight / height ** 2 )

print('=' * 80)
if bmi >= BMI_CLINICALLY_OBESE:
    print( BMI_CLINICALLY_OBESE_MSG.format(bmi) )

elif bmi > BMI_OBESE:
    print( BMI_OBESE_MSG.format(bmi) )

elif bmi > BMI_OVERWEIGHT:
    print( BMI_OVERWEIGHT_MSG.format(bmi) )

elif bmi > BMI_NORMAL:
    print( BMI_NORMAL_MSG.format(bmi) )

else:
    print( BMI_UNDERWEIGHT_MSG.format(bmi) )
print('=' * 80)


# Test cases:
#       BMI_CLINICALLY_OBESE
#           height: 1.8 m
#           weight: 120 kg
#       BMI_OBESE
#           height: 1.8 m
#           weight: 99.3 kg
#       BMI_OVERWEIGHT
#           height: 1.8 m
#           weight: 85 kg
#       BMI_NORMAL
#           height: 1.8 m
#           weight: 69
#       BMI_UNDERWEIGHT
#           height: 1.8 m
#           weight: 51
