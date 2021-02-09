import random
from os import system
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    return random.choices(cards, k=2)

def hit_me():
    return random.choice(cards)

def current_score():
    print(f"Your cards: {your_hand}, current score: {sum(your_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}")

def check_for_bust(hand):
    global bust
    if sum(hand) > 21 and 11 not in hand:
        bust = True
        return hand
    elif sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        return hand
    else:
        return hand

def the_winner_is():
    print(f"Your final hand: {your_hand}, final score: {sum(your_hand)}")
    print(f"Computer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")
    if sum(dealer_hand) == 21 and len(dealer_hand) == 2:
        print("Dealer has blackjack!")
    elif sum(your_hand) == 21 and len(your_hand) == 2:
        print("You have blackjack!")
    elif sum(your_hand) > 21:
        print("You bust!")
    elif sum(dealer_hand) > 21:
        print("Dealer busts!")
    elif sum(dealer_hand) > sum(your_hand):
        print("You lose!")
    elif sum(dealer_hand) < sum(your_hand):
        print("You win!")
    else:
        print("It's a draw!")
    
while input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'.lower():
    system('cls')
    print(art.logo)
    bust = False
    dealer_hand = deal()
    your_hand = deal()
    if sum(dealer_hand) == 21 or sum(your_hand) == 21:
        the_winner_is()
    else:
        current_score()
        while input("Type 'y' to get another card, type 'n' to pass: ") == 'y'.lower(): 
            your_hand.append(hit_me())
            your_hand = check_for_bust(your_hand)
            if bust == True:
                break
            else:
                current_score()
        if bust == False:
            while sum(dealer_hand) < 17:
                dealer_hand.append(hit_me())
                dealer_hand = check_for_bust(dealer_hand)
        the_winner_is()