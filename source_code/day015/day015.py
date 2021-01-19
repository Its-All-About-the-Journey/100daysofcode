# Grant Armstrong
# Day 15 Coffee Machine Application
# 01/19/2021

from data import MENU, resources


# Function to print report of remaining resources
def report():
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
	print(f"Money: ${resources['money']:,.2f}")


# Function to check if there are sufficient resources
def check_resources(selection):
	drink = MENU[selection]
	flag = True
	for ingredient, quantity in drink['ingredients'].items():
		if quantity > resources[ingredient]:
			print(f"Sorry there is not enough {ingredient}")
			flag = False
	return flag


# Function to deduct resources after making coffee
def deduct_resources(selection):
	drink = MENU[selection]
	for ingredient, quantity in drink['ingredients'].items():
		resources[ingredient] -= quantity


# Function to prompt user for payment - calls deduct_resources if there's enough monies
def payment(selection):
	drink = MENU[selection]
	print("Please insert coins...")
	quarters = 0.25 * int(input("Enter total number of quarters: "))
	dimes = 0.10 * int(input("Enter total number of dimes: "))
	nickels = 0.05 * int(input("Enter total number of nickels: "))
	pennies = 0.01 * int(input("Enter total number of pennies: "))
	total = quarters + dimes + nickels + pennies
	cost = drink["cost"]
	change = total - cost
	if total < cost:
		print("Sorry that's not enough money. Money refunded.")
		return
	elif total >= cost:
		resources["money"] += cost
		deduct_resources(selection)
		print(f"Here is ${change:,.2f} in change.\nHere is your {selection} ☕ Enjoy!")
		return


# Function that ties everything together and runs the other functions
def run_machine():
	while True:
		user_selection = input("What would you like? Enter espresso/latte/cappuccino: ").lower()


		# If the user selected report, show them a report
		if user_selection == 'report':
			report()
			continue
		# If the user selected exit, exit the application
		elif user_selection in ['off', 'exit']:
			print("Powering down...")
			exit()
		# Check to make sure the user entered a proper selection
		elif user_selection not in MENU.keys():
			print("Invalid selection. Please try again...")
			continue

		# Check to see if there are available resources for the users selection - run payment function if there are
		if check_resources(user_selection):
			payment(user_selection)  # payment function also runs the deduct_resources() function\


run_machine()
