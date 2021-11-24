# Grant Armstrong
# 01/12/2021
# Day011 Blackjack Game

import os
import random
import time
from termcolor import colored
import cards

points = {'ace': 11, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
          'ten': 10, 'jack': 10, 'queen': 10, 'king': 10}

wl = {'wins': 0, 'losses': 0, 'ties': 0}


# Function will clear command prompt window on Linux and Windows machines
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to deal a card from deck to player and remove it from the deck
def deal_card(current_deck):
    card = random.choice(current_deck)
    current_deck.remove(card)
    return card


# Function returns the total score of the handed that is passed in (returns multiple scores if hand includes an Ace)
# Will return final score if final=True
def score_hand(hand, final=False):
    hand_sum = 0
    high_sum = 0
    # Return sum of hand that doesn't contain an Ace
    if 'ace' not in hand:
        for card in hand:
            hand_sum += points[card]
        return hand_sum
    # Return tuple of potential scores if hand contains an Ace
    elif 'ace' in hand:
        for card in hand:
            high_sum += points[card]
        low_sum = high_sum - 10
        # Return both scores if this isn't the final scoring
        if not final:
            return low_sum, high_sum
        # Return highest score that is <= 21 if this is the final scoring
        else:
            return high_sum if high_sum <= 21 else low_sum


# Function to display the final cards and scores
def display_final_scores(players_hand, computers_hand):
    cards.display_all_cards(players_hand)
    print('Players Final Cards')
    print(f'Players Final Score: {score_hand(players_hand, final=True)}')

    cards.display_all_cards(computers_hand)
    print('Dealers Final Cards')
    print(f'Dealers Final Score: {score_hand(computers_hand, final=True)}')


# Function that checks if hand is Blackjack or not
def is_blackjack(hand):
    if score_hand(hand, final=True) == 21 and len(hand) == 2:
        return True
    else:
        return False


# Function to print winning messages
def print_msg(message, category):
    if category == 'w':
        print(colored(message, 'green', attrs=['blink', 'bold']))
    elif category == 'l':
        print(colored(message, 'red', attrs=['blink', 'bold']))
    elif category == 't':
        print(colored(message, 'yellow', attrs=['blink', 'bold']))
    elif category == 'g':
        print(colored(message, 'white', attrs=['bold']))


# Flags
playing = 'y'
answered = False
no_math = 'no'

while playing.lower() in ['y', 'yes']:
    clear()
    print(cards.logo, '\n')

    # Ask user how many decks and if they want their score auto-displayed for them
    # Validate the answer
    while not answered:
        num_decks = int(input("Enter many decks of cards would you like to play with (1-5): "))
        no_math = input("Do you want the system to auto-calculate your score? Type 'y' or 'n': ")
        if num_decks in [1, 2, 3, 4, 5] and no_math in ['y', 'yes', 'n', 'no']:
            game_deck = cards.deck * num_decks
            random.shuffle(game_deck)
            answered = True
            print('\n')
        else:
            print("Invalid answer(s). Please try again...")

    # Check that there is a sufficient number of cards left in the deck to finish the round
    if len(game_deck) < 8:
        print("There are insufficient cards remaining in the deck to start a new round.")
        print("Please start a new game!")
        exit()

    print_msg('Dealing...', 'g')
    time.sleep(1.5)

    # Deal the computer and player their initial hands from the game deck
    player_hand = [deal_card(game_deck), deal_card(game_deck)]
    computer_hand = [deal_card(game_deck), deal_card(game_deck)]

    # Display the player and dealers starting hands - only show part of the dealers hand
    cards.display_all_cards(player_hand)
    print("Your Cards")

    # Only print the player score if they asked for that
    if no_math in ['y', 'yes']:
        print(f'Current Score: {score_hand(player_hand)}')

    cards.display_visible_cards(computer_hand)  # Only show part of the computers hand
    print("Dealers Cards")

    # Loop that will run if the player decides to hit
    hitting = True
    while hitting:

        # If either the player or the dealer has Blackjack right away, grant them the win
        if is_blackjack(player_hand) and not is_blackjack(computer_hand):
            print_msg('\nSomeone got lucky...\n', 'g')
            time.sleep(2)
            display_final_scores(player_hand, computer_hand)
            print_msg('Blackjack! You win the round! Much fast, so wow.', 'w')
            wl.update({'wins': wl.get('wins') + 1})
            break
        elif not is_blackjack(player_hand) and is_blackjack(computer_hand):
            print_msg('\nSomeone got lucky...\n', 'g')
            time.sleep(2)
            display_final_scores(player_hand, computer_hand)
            print_msg('Dealer has Blackjack. You lost! That was fast...', 'l')
            wl.update({'losses': wl.get('losses') + 1})
            break
        elif is_blackjack(player_hand) and is_blackjack(computer_hand):
            print_msg("\nAs luck would have it...\n")
            time.sleep(2)
            display_final_scores(player_hand, computer_hand)
            print_msg('Both you and the dealer have Blackjack! The round is a push!', 't')
            wl.update({'ties': wl.get('ties') + 1})
            break

        # Ask the player if they wish to hit or stay
        hit = input("\nType 'hit' to get another card, type 'stay' to pass: ")

        # If the player decides to hit, append another card to their hand
        if hit.lower() in ['hit', 'yes', 'y']:
            player_hand.append(deal_card(game_deck))
            print_msg("\nHitting...", 'g')
            time.sleep(1.5)
            cards.display_all_cards(player_hand)
            print("Your Cards")
            # Only print the player score if they asked for that
            if no_math in ['y', 'yes']:
                print(f'Current Score: {score_hand(player_hand)}')
            time.sleep(3)

            # If the user busts they lose immediately
            if score_hand(player_hand, final=True) > 21:
                print_msg('\nUh oh...', 'g')
                time.sleep(3)
                display_final_scores(player_hand, computer_hand)
                print_msg('You went over. You lose!', 'l')
                wl.update({'losses': wl.get('losses') + 1})
                break

        # The sequence if the player chooses to stay
        elif hit.lower() in ['stay', 'no', 'n']:
            stay_message = random.choice(["\nThat's a bold strategy Cotton. Let's see if it pays off...",
            "\nYou have chosen to stay...", "You are staying..."])
            if score_hand(player_hand, final=True) <= 15:
                stay_message = f"Staying on {score_hand(player_hand, final=True)}, eh? Good luck..."
            print_msg(stay_message, 'g')
            time.sleep(1.5)

            # Suspenseful reveal of the computers hand
            print_msg('\nThe dealer reveals his hand...', 'g')
            time.sleep(2)
            cards.display_all_cards(computer_hand)
            time.sleep(3)

            # Let the computer hit until its satisfied with its hand (17 or over)
            while score_hand(computer_hand, final=True) < 17:
                print_msg("\nThe dealer hits...", 'g')
                computer_hand.append(deal_card(game_deck))
                time.sleep(1.5)
                cards.display_all_cards(computer_hand)
                print("Dealers Cards")
                time.sleep(3)
            if score_hand(computer_hand, final=True) <= 21:
                print_msg("\nThe dealer is staying...", 'g')
            time.sleep(1.5)

            # Finally, compare the computers hand to the players hand and report outcome
            player_final_score = score_hand(player_hand, final=True)
            computer_final_score = score_hand(computer_hand, final=True)
            display_final_scores(player_hand, computer_hand)

            if player_final_score <= 21 >= computer_final_score:
                if player_final_score == computer_final_score:
                    print_msg("\nYou have tied. The round is a push!", 't')
                    wl.update({'ties': wl.get('ties') + 1})
                elif player_final_score > computer_final_score:
                    print_msg('\nYou beat the dealer!', 'w')
                    wl.update({'wins': wl.get('wins') + 1})
                else:
                    print_msg('\nThe dealer wins!', 'l')
                    wl.update({'losses': wl.get('losses') + 1})
                break

            elif player_final_score <= 21 < computer_final_score:
                print_msg('\nThe dealer busted! You win!', 'w')
                wl.update({'wins': wl.get('wins') + 1})
                break
            elif computer_final_score <= 21 < player_final_score:
                print_msg('\nYou busted! The dealer wins!', 'l')
                wl.update({'losses': wl.get('losses') + 1})
                break

    playing = input("\nDo you want to play another game of Blackjack? Type 'y' or 'n': ")

print(f"\nTotal Wins: {wl.get('wins')} \nTotal Losses: {wl.get('losses')} \nTotal Draws: {wl.get('ties')}")
