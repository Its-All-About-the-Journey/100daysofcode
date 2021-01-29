#!/usr/bin/env python3
# 100 Days of Code : Day 9 Project
# Silent Auction
# Adam Pawlowski (@hypermanganate)

from art import logo
import os

def clear():
# Clear Screen
  if os.name == "posix":
    # Should be valid for Mac/Linux
    os.system('clear')
  else:
    # Should work on Windows
    os.system('cls')

def check_bid(bid):
  if bid < 1:
    return False

  return True

# Main

more_bidders = True
high_bid = 0
high_bidder = ''
auction = {}

while more_bidders:

  clear()
  print(logo)
  print("Welcome to the secret auction program.")
  bidder = input("What is your name?: ")
  bid = -1
  while not check_bid(bid):
    bid = int(input("What's your bid?: $"))
  auction[bidder] = bid
  if input("Are there any other bidders? Type 'yes' or 'no'. ").lower() == "no":
    more_bidders = False

clear()
for bidder in auction:
  if auction[bidder] > high_bid:
    high_bidder = bidder
    high_bid = auction[bidder]

print(f"""The auction has been won by {high_bidder}, with a high bid of ${high_bid}.""")

