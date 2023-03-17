# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Number of items in the list minus 1 to account for list starting at 0
numofnames = len(names) - 1
#Assign the name at a random position in the names list to ranname variable
ranname = names[random.randint(0,numofnames)]
#Tell the user which random person will buy the meal today
print(f"{ranname} is going to buy the meal today!")