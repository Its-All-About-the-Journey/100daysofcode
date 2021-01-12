from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def bust():
    print("You bust. Game over\n")

def hand_total(hand):
    total = 0
    for card in range(0, len(hand)):
        total = total + hand[card]
    #print(f'total check = {total}')
    return total

def dealer_check(hand, handTotal):
    while handTotal < 17:
        new_card = random.choice(cards)        
        hand.append(new_card)
        handTotal = hand_total(hand)

def compare_hands(userTotal, computerTotal):
    if computerTotal > 21:
        print(f"The computer busts with a hand of {computerTotal}! You win with a hand of {userTotal}")
    elif computerTotal > userTotal:
        print(f"The computer wins with a hand of {computerTotal}")
    elif computerTotal == userTotal:
        print(f"The game ends in a draw.")
    else:
        print(f"The computer has a hand of {computerTotal}. You win with a hand of {userTotal}!")

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
        #print(f"Hand is {handTotal}\n")
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
            bustCheck = check_for_bust(hand, handTotal)
            print(f"\nNew hand = {hand} = {handTotal}\n")
            if bustCheck == "bust":
                return "bust"
        else:
            print("")
            keepDrawing = False
    
def blackjack():
    print(logo)
    user = ['','']
    user[0] = random.choice(cards)
    user[1] = random.choice(cards)

    computer = ['','']
    computer[0] = random.choice(cards)
    computer[1] = random.choice(cards)

    userTotal = user[0] + user[1]
    computerTotal = computer[0] + computer[1]
    print(f"Your hand: {user} = {userTotal}\n")
    print(f"Dealer hand: {computer} = {computerTotal}\n")

    blackjackCheck = check_for_blackjack(user, userTotal, computer, computerTotal)
    if blackjackCheck == "user_wins":
        print("You got a blackjack! You win!\n")
        return
    elif blackjackCheck == "computer_wins":
        print("The house has a Blackjack, you lose\n")
        return

    ### Check to see if the user busts ###
    ### Probably can add most of this into the function ###
    userBustCheck = check_for_bust(user, userTotal)
    if userBustCheck == "bust":
        bust()
        return
    else:
        userFinal = new_card_check(user, userTotal)
        userTotal = hand_total(user)
        if userFinal == "bust":
            bust()
            return
    ######################################
    
    ### dealer section ###
    dealer_check(computer, computerTotal)
    computerTotal = hand_total(computer)
    ######################

    ### compare hands ###
    winner = compare_hands(userTotal, computerTotal)
    #####################

        
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