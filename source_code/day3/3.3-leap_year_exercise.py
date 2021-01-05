# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆
                                                            #LY     #LY
# on every year that is evenly divisible by 4               True    True
#   except every year that is evenly divisible by 100       False   False
#       unless the year is also evenly divisible by 400     True    False

#Write your code below this line 👇

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

