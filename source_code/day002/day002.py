print('Welcome to the tip calculator!')
total = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))/100
people = int(input('How many people will split the bill? '))
split = round((total + (total * tip))/people, 2)
print(f'Each person should pay: ${split}')