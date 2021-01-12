"""
Day 011 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/11/2021

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""

import random
import os
import sys

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards_to_count):
    """Returns the sum of cards in hand"""
    score = sum(cards_to_count)
    # Check to see if blackjack is dealt in first deal
    if score == 21 and len(cards_to_count) == 2:
        return 0
    # Check to see if ace is counted as 11 and swap to 1 if score is over 21
    if 11 in cards_to_count and sum(cards_to_count) > 21:
        cards_to_count.remove(11)
        cards_to_count.append(1)
    return score


def compare(user, computer):
    """Takes the scores of the user and computer and compare to find winner"""
    if user == computer:
        return "Its a Draw."
    elif computer == 0:
        return "The computer has Blackjack, you lose."
    elif user == 0:
        return "You win with Blackjack!"
    elif user > 21:
        return "You busted!"
    elif computer > 21:
        return "The computer busted, you WIN!"
    elif user > computer:
        return "You win!"
    else:
        return "You lose."


def play_game():
    print(logo)
    # Deal initial cards
    user_cards = []
    computer_cards = []
    end_of_game = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Rechecking score
    while not end_of_game:
        # Evaluating initial score
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, and current score: {user_score}.")
        print(f"Computers first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            end_of_game = True
        else:
            keep_playing = input("Would you like to draw another card? Enter 'Y' for yes, 'N' for No: ").lower()
            if keep_playing == "y":
                user_cards.append(deal_card())
            else:
                end_of_game = True

    # User done, dealing computers cards
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("clear")
    play_game()