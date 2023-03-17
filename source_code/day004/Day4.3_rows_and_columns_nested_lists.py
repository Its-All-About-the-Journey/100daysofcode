# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Setup variables that give you the numbers entered by the user -1 for list indexes
col = int(position[0]) -1
row = int(position[1]) - 1
#Modify the map variable (nested list) to set the X at the row and column specified.  Careful to specify the positions in the correct order since map is a list of rows, you have to pick the row first, then you're picking the 'column of that row'.
map[row][col] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

