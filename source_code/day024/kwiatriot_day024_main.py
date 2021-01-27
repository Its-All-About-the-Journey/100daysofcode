"""
Day 024 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/26/2021, 1/23/2021
"""
# Basic operation of open as 'read only'
with open("../../../../../Documents/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Use the keyword argument 'mode' to specify as  read 'r', write 'w', append 'a'
# with open("my_file.txt", mode='a') as file:
#     file.write("\nThis is the newly added text!")

# With the write mode, if the file doesnt exist it will create it
