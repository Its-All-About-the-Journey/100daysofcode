# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# You are going to write a program which will mark a spot with an X.
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# First your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x".

#Write your code below this row 👇
horizontal = int(position[0])
vertical = int(position[1])

# Method 1
selected_row = map[vertical -1]
selected_row[horizontal -1] = "X"

# Method 2
map[vertical -1][horizontal -1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")