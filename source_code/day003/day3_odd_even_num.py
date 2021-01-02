number = int(input("Which number do you want to check? "))

result = number % 2

if result != 0:
    print("This is a odd number")
else:
    print("This is an even number")