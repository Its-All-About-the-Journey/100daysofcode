"""
Day 004 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/4/2021
"""

import random

# Ex. 4.1 - Coin toss

coin_toss = random.randint(0, 1)

if coin_toss == 0:
    print("Heads")
else:
    print("Tails")

# Ex. 4.2 - Random Bill paying

names_string = input("Give me everybody's names, separated by a comma. ")
# splitting the string on a comma and space to get just the names
names = names_string.split(", ")
# getting length of names added by the user
names_length = len(names)
# making a random selection
bill_payer = random.randrange(0, names_length)
print(f"{names[bill_payer]} is going to buy the meal tonight.")

# Ex. 4.3 - Choosing where to bury the treasure
# Creating the blank treasure map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
treasure_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# turning the string into indexable numbers
col = int(position[0])
row = int(position[1])
# changing the users position into an X
treasure_map[row - 1][col - 1] = "X"
# printing new map
print(f"{row1}\n{row2}\n{row3}")
