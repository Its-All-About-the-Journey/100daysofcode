# 4.1 - coin flip
# ---------------------------------------
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

from random import randint

heads = tails = 0
# flip 1 million coins and generate a histogram of the outcomes
for _ in range(1_000_000):
  r = randint(0, 1)
  heads += r     # increment by r
  tails += r ^ 1 # increment by the opposite of r

print(f"Heads ({heads}) {'○' * (heads//10_000)}")
print(f"Tails ({tails}) {'●' * (tails//10_000)}")

# 4.2 - who pays?
# ---------------------------------------
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

from random import randint

who = randint(0, len(names) - 1)

print(f"{names[who]} pays")

# 4.3 - treasure map
# ---------------------------------------
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# take 2-digit input as string
# split each digit into own list element
# converting each to int
# and subtract 1 from each for 0-indexing
col, row = [int(p) - 1 for p in list(position)]

# place marker on map
map[row][col] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")