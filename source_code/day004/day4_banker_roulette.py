import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

numb_friend = len(names)
friend = random.randint(0, numb_friend - 1)

print(names[friend] + " is going to buy the meal today!")