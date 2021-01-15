import random
import os
from game_data import data
from source_code.day014.art import logo, versus


# Function will clear command prompt window on Linux and Windows machines
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


# Function to get a random user from data, display their information and remove them from data
def get_person():
	random.shuffle(data)
	person = data.pop()
	return person


# Function to get users guess and validate it
def get_guess():
	while True:
		user_guess = input("Who has more followers? Type 'A' or 'B': ")
		if user_guess.lower() in ['a', 'b']:
			break
		else:
			print("Invalid Selection. Try Again...")
			continue
	return user_guess


# Function prints person A versus person B - it also returns their total respective follower counts
def compare_people(pa, pb):
	print(f"Compare A: {print_person_info(pa)}")
	print(versus)
	print(f"Against B: {print_person_info(pb)}")
	return person_A['follower_count'], person_B['follower_count']


# Pass in a person dictionary and it display the info as required
def print_person_info(p):
	return f"{p['name']}, a {p['description']} from {p['country']}"


score = 0
person_A = None
person_B = None

while True:
	print(logo)

	# If it is first round, get 2 new people, otherwise switch B to A and get new B
	if score != 0:
		print(f"You're right! Current score: {score}")
		person_A = person_B
		person_B = get_person()
	elif score == 0:
		person_A = get_person()
		person_B = get_person()

	# Print out the versus information and get the total followers of each person for comparison
	follows_A, follows_B = compare_people(person_A, person_B)

	# Get the users guess on whether 'A' or 'B' has more followers
	guess = get_guess()

	# Make comparison, add to score if correct and restart - otherwise, end game
	if (guess.lower() == 'a' and (follows_A > follows_B)) or (guess.lower() == 'b' and (follows_B > follows_A)):
		score += 1
		clear()
	else:
		clear()
		print(f"Sorry, that's wrong. Final score: {score}")
		break






