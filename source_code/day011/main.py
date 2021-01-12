#!/usr/bin/env python3
# 100 Days of Code : Day 11 Project
# Blackjack
# Adam Pawlowski (@hypermanganate)

# 1 Deck
# Each Player - Two Cards
# Player Plays First

import random
import os
from art import logo

# Setup

suits = ['♥', '♦', '♣', '♠']
values = []
for iter in range(2, 11):
  values.append(iter)
values += [10, 10, 10, 11]

# Build Card Deck
def get_deck():
  """
  Returns a "deck"tionary of cards.
  """
  deck = {}
  deck['stack'] = []
  for iter in range(0, 52):
    deck[iter] = { 'suit': None, 'value': None }
    deck['stack'].append(iter)
  card = 0
  # This is a computer, so all of these things can be numerical, but, it is not human readable or understandable.
  # For brevity, this is done numerically here.
  for suit in [0, 1, 2, 3]: # Hearts, Diamons, Clubs, Spades
    for iter in range(2, 15):  # 2 - 10, 11: Jack, 12: Queen: 13: King: 14: Ace
      deck[card]['suit'] = suit
      deck[card]['value'] = iter
      card += 1
#    for face_card in ['Jack', 'Queen', 'King', 'Ace']:
#      deck[card]['suit'] = suit
#      deck[card]['value'] = face_card
#      print(f"""Card {card} is a {face_card} of {suit}""")
#      card += 1

# Initially I wrote it like this, but, soon realized that selecting a random card out of this was going to be a pain in the ass.
#
#  # Suits
#  deck = { "Hearts": [], "Diamonds": [], "Clubs": [], "Spades": [] }
#  # Cards
#  for suit in deck:
#    # Numeric Cards
#    for iter in range(2, 10):
#       print(type(iter))
#       deck[suit].append(iter)
#    # Face Cards
#    deck[suit] += ["Jack", "Queen", "King", "Ace"]

  return deck

# Get a random card
def get_card(stack):
  """
  Return a random card from the deck stack, and remove it from the deck.
  """

  if len(stack) == 0:
    print("Error - deck has no cards!")
    exit()


  card = stack[random.randint(0, len(stack) - 1)]
  stack.remove(card)
  return stack, card

# Get the printable string of a given card in the deck
def get_card_string(deck, card):
  """
  Format the playing card in a printable useful way and return it.
  """
  suit = suits[deck[card]['suit']]
  value = deck[card]['value']
  if value == 11:
    value = "J"
  elif value == 12:
    value = "K"
  elif value == 13:
    value = "Q"
  elif value == 14:
    value = "A"

  return f"{value}{suit}"

# A print out of the "hands"
def print_hand(player, computer):
  """
  Prints the player's hands out for the game display.
  """

  print(f"""Your hand: {' '.join(player['print'])} ({compute_hand_value(player['comp'])})""")
  print(f"""Their hand: {' '.join(computer['print'])} ({compute_hand_value(computer['comp'])})""")

  return None

# Add up all the cards
def compute_hand_value(hand):

  this_hand = hand

  this_hand.sort()
  aces = []

  while 14 in this_hand:
    aces.append("ace")
    this_hand.pop(hand.index(14))

  value = 0
  for card in this_hand:
    if card <= 10:
      value += card
    else:
      value += 10

  for ace in aces:
    this_hand.append(14)
    if value > 10:
      value += 1
    else:
      value += 11

  return value


# Program Launch Confirmation
def in_or_out():
  """
  Prompt the user to decide, yes or no, if they'd like to play a game of blackjack.
  If yes, return.
  If no, exit.
  """
  proceed = None # Initial value
  while proceed not in ['y', 'n']:
    # Prompt
    proceed = input("Do you want to play a game of blackjack? (y/n) ").lower()

  # Process value
  if proceed == 'y':
    return True
  else:
    return False

# Deal a card
def deal(deck, hand):
  """
  Deals a card from a supplied deck, to a player's hand.
  """
  deck['stack'], card = get_card(deck['stack'])
  hand['comp'].append(deck[card]['value'])
  hand['print'].append(get_card_string(deck, card))

  return deck, hand

# Check if the hand has busted
def check_bust(hand):
  """
  Compute if the hand value is over 21, which is a bust.
  """
  if compute_hand_value(hand) > 21:
    return True
  return False

def check_win(hand):
  """
  Compute if the hand value is exactly 21, which is a win.
  """
  if compute_hand_value(hand) == 21:
    return True
  return False

# Check if the game should progress
def game_progress(hand_player, hand_computer):

  player_bust = check_bust(hand_player['comp'])
  computer_bust = check_bust(hand_computer['comp'])

  player_win = check_win(hand_player['comp'])
  computer_win = check_win(hand_computer['comp'])

  if player_bust or computer_bust:
  # Someone busted, game has ended.
    if player_bust:
       print("Game over! You busted!")
       return False
    if computer_bust:
       print("You won! The computer busted!")
       return False

  if player_win or computer_win:
    if player_win:
       print("BLACKJACK! You've won!")
       return False
    if computer_win:
       print("Computer gets Blackjack, sorry!")
       return False

  return True

# Main Game Loop
def play_game():

  # Hands
  hand_player = { 'print' : [], 'comp' : [], 'score' : 0 }
  hand_computer = { 'print' : [], 'comp' : [], 'score' : 0 }

  # Get a deck of cards
  deck = get_deck()

  # Get the starting hand
  deck, hand_player = deal(deck, hand_player)
  deck, hand_computer = deal(deck, hand_computer)
  deck, hand_player = deal(deck, hand_player)

  my_turn = True
  printed = False
  print("The game begins...")
  while game_progress(hand_player, hand_computer):
    clear()
    print(logo)
    print_hand(hand_player, hand_computer)
    if not my_turn:
      if compute_hand_value(hand_computer['comp']) < compute_hand_value(hand_player['comp']):
        deck, hand_computer = deal(deck, hand_computer)
        print (f"Computer was dealt: {hand_computer['print'][-1]}.")
      else:
        clear()
        print(logo)
        print_hand(hand_player, hand_computer)
        print(f"Computer's hand wins! You should have hit!")
        printed = True
        break
    else:
        choice = None
        while choice not in ['y', 'n']:
          choice = input("Would you like another card? (y/n)")
        if choice == 'y':
          deck, hand_player = deal(deck, hand_player)
          print (f"You were dealt: {hand_player['print'][-1]}.")
        else:
          my_turn = False

    if not printed:
      clear()
      print(logo)
      print("The cards were:")
      print_hand(hand_player, hand_computer)

def clear():
  if os.name == "posix":
    os.system("clear")
  else:
    os.system("cls")

# Main

# Prompt user to confirm they'd like to play
if not in_or_out():
  # User has declined
  exit()

while True:
  clear()
  play_game()
  answer = None
  while answer not in ['y', 'n']:
    answer = input("Would you like to play again? (y/n) ")
  if answer == "n":
    break
