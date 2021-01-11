from art import logo
import random

print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def check_for_blackjack(user, userTotal, computer, computerTotal):
    if userTotal == 21:
        print("Congratulations, you got a Blackjack! You win!")
        return True
    elif computerTotal == 21:
        print("The house has a Blackjack, you lose")
        return True
    elif userTotal > 21:
        for i in user:
            if i == 11:
                userTotal = userTotal - 10
                if userTotal > 21:
                    print("You are over 21, you lose")
                    return "lose"
        else:
            print("You are over 21, you lose")
            return "lose"
    else:
        another_card = input("Do you want another card? 'Y' or 'No': ")
        if another_card == 'y':
            new_card(user, computer)

def new_card(user, userTotal, computer, computerTotal):
    user = user.extend(random.choice(cards)
    #print(user)

def blackjack():
    in_progress = True
    while in_progress:
        user = ['','']
        user[0] = random.choice(cards)
        user[1] = random.choice(cards)
        #user = user.append(random.choice )
        computer = ['','']
        computer[0] = random.choice(cards)
        computer[1] = random.choice(cards)

        userTotal = user[0] + user[1]
        computerTotal = computer[0] + computer[1]

        print(userTotal, computerTotal)

        in_progress == True
        if check_for_blackjack(userTotal, computerTotal) == True:
            break
        else:
            next_round = new_card(userTotal, computerTotal)
            if next_round == "lose":
                in_progress = False
                
    if input("Would you like to keep playing? 'y' or 'no': ") == 'y':
        blackjack()
    else:
        return    

choice = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
if choice == "y":
    blackjack()