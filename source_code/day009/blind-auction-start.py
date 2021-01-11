import os
#HINT: You can call clear() to clear the output in the console.
from art import logo

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}")

print(logo)
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name: ")
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')