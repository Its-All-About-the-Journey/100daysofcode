# Grant Armstrong
# 1/11/2021
# 100DaysOfCode Challenge
# Day009 Secret Auction Program

from art import logo
import os

print(logo, '\nWelcome to the secret auction program.\n')


# Function will clear command prompt window on Linux and Windows machines
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
	return ''


# Function to get the highest bid and that bidders name
def get_highest_bid(bidders_dict):
	highest_bid = max(bidders_dict.values())
	highest_bidder = [k for k, v in bidders_dict.items() if v == highest_bid]
	# If only 1 person has the highest bid, else if 2 or more people bid the same highest bid
	if len(highest_bidder) == 1:
		print(f'The winner is {highest_bidder[0]} with a bid of ${highest_bid:,.2f}')
	else:
		print(f'The winners are {" and ".join(highest_bidder)} each with a bid of ${highest_bid:,.2f}')


# Function asks for bidder name and amount and adds to bidders list as dictionary item
def add_bid():
	bidders = {}
	bidding = True
	while bidding:
		name = input("What is your name?: ")
		bid = float(input("What is your bid?: $"))
		bidders[name] = bid
		# This loop will verify user inputs and decide whether to run the outer loop again or not
		while True:
			again = input("Are there any other bidders? Type 'yes' or 'no'. ")
			if again.lower() not in ['yes', 'y', 'no', 'n']:
				print("Invalid entry. Try again...")
				continue
			if again.lower() in ['no', 'n']:
				bidding = False
				clear()
				break
			elif again.lower() in ['yes', 'y']:
				bidding = True
				clear()
				break
	# Get the highest bidder and display the name/bid
	get_highest_bid(bidders)


add_bid()


