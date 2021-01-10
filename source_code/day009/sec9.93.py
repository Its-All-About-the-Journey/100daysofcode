import os

from art import logo

# Clear the terminal screen
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

# Get a single user bid
def get_user_input() -> dict:
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))

    return {
        'name': name,
        'bid': bid
    }

another_user = True
user_list = list()

# Get all users bid
while another_user:

    print(logo)

    user_list.append( get_user_input() )

    more_bidders = input('Are there any other bidders? Type yes or no. ')[0].lower()
    
    if  more_bidders == 'n' or more_bidders != 'y':
        another_user = False

    clear()

# No winner yet
highest_bid = {'name': 'No winner', 'bid': 0}

# Find winner
for user in user_list:
    if user['bid'] > highest_bid['bid']:
        highest_bid = user   

print(f'The winner is {highest_bid["name"]} at ${highest_bid["bid"]}.')