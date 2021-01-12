# Grant Armstrong
# 1/12/2021
# Day010 Calculator Application

from art import logo
import os


# Function will clear command prompt window on Linux and Windows machines
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


# Function will perform the calculation based on user inputs
def calculate(n1, n2, symbol):
	if symbol == '+':
		return n1 + n2
	if symbol == '-':
		return n1 - n2
	if symbol == '*':
		return n1 * n2
	if symbol == '/':
		return n1 / n2


# Function handles the logic behind running the calculate function
def run_calculation():
	clear()
	print(logo)

	num1 = float(input("What is the first number?: ")) # get num1

	# Loop will run from here if user wants to continue using the previously calculated answer
	while True:
		print("\n+\n-\n*\n/") # Print out the symbols
		operation_symbol = input("\nPick an operation from the line above: ")

		# Check to make sure the user entered a valid operational symbol
		while True:
			if operation_symbol not in ['+', '-', '*', '/']:
				print(f"\nYou have entered an invalid operation '{operation_symbol}'. Please try again...")
				operation_symbol = input("Pick an operation (+, -, * or /): ")
			else:
				break

		num2 = float(input("\nWhat is the next number?: ")) # get num2

		answer = calculate(num1, num2, operation_symbol) # calculate the answer

		print(f'\n{num1} {operation_symbol} {num2} = {answer}') # print the answer

		# Determine if the user wishes to continue the calculation or start new
		continue_calc = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
		if continue_calc.lower() in ['n', 'no']:
			run_calculation()
		elif continue_calc.lower() in ['y', 'yes']:
			num1 = answer
			continue


run_calculation() # run the program

