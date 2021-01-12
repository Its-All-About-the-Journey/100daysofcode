from art import logo
import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def bust():
    print("You bust. Game over")

def dealerCheck(hand, handTotal):
    while handTotal < 17:
        new_card = random.choice(cards)        
        hand.append(new_card)
        handTotal = hand_total(hand)

def hand_total(hand):
    total = 0
    for card in range(0, len(hand)):
        total = total + hand[card]
    return total

def check_for_blackjack(user, userTotal, computer, computerTotal):
    if userTotal == 21:
        return "user_wins"
    elif computerTotal == 21:        
        return "computer_wins"

def check_for_bust(hand, handTotal):
    if handTotal > 21:
        for card in range(0, len(hand)):
            if hand[card] == 11:
                hand[card] = 1
        handTotal = hand_total(hand)
        print(f"Hand is {handTotal}")
        if handTotal > 21:           
            return "bust"

def new_card_check(hand, handTotal):
    keepDrawing = True
    while keepDrawing:
        new_card_choice = input(f"Your current hand is: {handTotal}. Would you like another card? 'Y' or 'N': ")
        if new_card_choice == 'y':
            new_card = random.choice(cards)        
            hand.append(new_card)
            handTotal = hand_total(hand)
            print(f"New hand = {hand} = {handTotal}")
            bustCheck = check_for_bust(hand, handTotal)
            if bustCheck == "bust":
                return "bust"
        else:
            keepDrawing = False
    
def blackjack():
    user = ['','']
    user[0] = random.choice(cards)
    user[1] = random.choice(cards)

    computer = ['','']
    computer[0] = random.choice(cards)
    computer[1] = random.choice(cards)

    userTotal = user[0] + user[1]
    computerTotal = computer[0] + computer[1]
    print(f"Your hand: {user} = {userTotal}")
    print(f"Dealer hand: {computer} = {computerTotal}")

    blackjackCheck = check_for_blackjack(user, userTotal, computer, computerTotal)
    if blackjackCheck == "user_wins":
        print("You got a blackjack! You win!\n")
        return
    elif blackjackCheck == "computer_wins":
        print("The house has a Blackjack, you lose\n")
        return

    userBustCheck = check_for_bust(user, userTotal)
    if userBustCheck == "bust":
        bust()
        return
    else:
        userFinal = new_card_check(user, userTotal)
        if userFinal == "bust":
            bust()
            return
    
    userTotal = hand_total(user)
    computerTotal = hand_total(computer)
    dealerCheck(computer, computerTotal)
    if computerTotal > 21:
        print(f"The computer busts with a hand of {computerTotal}! You win with a hand of {userTotal}")
    elif computerTotal > userTotal:
        print(f"THe computer wins with a hand of {computerTotal}")
    else:
        print(f"You win with a hand of {userTotal}!")

#####
        
user_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
if user_choice == "y":
    blackjack()

keep_playing = True
while keep_playing:
    if input("Would you like to keep playing? 'y' or 'no': ") == 'y':
        blackjack()
    else:
        print("\nThank you for playing!")
        keep_playing = False