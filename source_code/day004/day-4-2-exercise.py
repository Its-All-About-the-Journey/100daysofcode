# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
#print(names)
name_count = len(names)
random_index = random.randint(0,(int(name_count)-1))
print(random_index)
print(f"{names[random_index]} is going to buy the meal today!")