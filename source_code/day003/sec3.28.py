# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 :
    print(f'{number} is an odd number.')
else:
    print(f'{number} is an even number.')


# Using an f-string to add inline code
# print( f'{number} is an {"odd" if number % 2 else "even"} number.')