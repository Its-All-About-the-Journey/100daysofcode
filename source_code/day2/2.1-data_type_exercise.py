# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# The output of the above code is a string
print(type(two_digit_number))

# convert string to an integer
num_char_1 = int(two_digit_number[0])
num_char_2 = int(two_digit_number[1])
print(type(num_char_1))

# add both integers
print(num_char_1 + num_char_2)

# Solution 🚨
# Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two digits togeter
two_digit_number = first_digit + second_digit

print(two_digit_number)