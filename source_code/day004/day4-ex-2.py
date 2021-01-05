# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

x = len(names) - 1

shake = random.randint(0,x)

who_pays = names[shake]

print(f"{who_pays} is going to buy the meal today.")

