#from replit import clear
from os import system
import art
#HINT: You can call clear() to clear the output in the console.

more_bidders = True
bids = {}
max_bid = 0
max_bidder = ""

print(art.logo)
print("Welcome to the secret auction program.")

while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    if input("Are there any other bidders? Type 'yes' or 'no'.\n").lower() == "no":
        break
    system('cls')

for bidder in bids:
    if bids[bidder] > max_bid:
        max_bidder = bidder
        max_bid = bids[bidder]
    
print(f"The winner is {max_bidder} with a bid of ${max_bid}.")
