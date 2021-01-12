############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

# final project - blackjack
# -----------------------------------------------------------------------------
from random import randint
from blackjackart import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_cards(count = 2):
    result = []
    for card in range(count):
        result.append(cards[randint(0, len(cards) - 1)])
    return result

while input("blackjack? (y/n): ") == "y":
    print(logo)
    print()

    # Get player1 starting hand
    player1 = get_cards()
    print(f"Your cards: {player1}, current score: {sum(player1)}")

    # get cpu1 starting hand, but show only 1 card
    cpu1 = get_cards()
    print(f"Computer's first card: {cpu1[0]}")

    # did player1 win immediately?
    if sum(player1) == 21:
        print("You Won!")
        continue

    # player1 hit or stand loop
    bust = False
    while input("hit or stand? (hit/stand): ") == "hit":
        player1.extend(get_cards(1))

        # try to convert any 11s (Aces) into 1s to avoid the bust
        while sum(player1) > 21 and 11 in player1:
            player1[player1.index(11)] = 1

        print(f"\nYou hit! Your cards: {player1}, current score: {sum(player1)}")

        # did player1 reach 21? if so, force a stand
        if sum(player1) == 21:
            break

        # did player1 bust? if so, force a loss
        if sum(player1) > 21:
            bust = True
            break

    # did player1 bust while hitting for more cards?
    if bust:
        print("\nYou bust! You lose!")
        continue

    # It's CPU's turn to crush this newb
    print()
    cpu_hit = False
    while sum(cpu1) < 17:
        cpu1.extend(get_cards(1))
        cpu_hit = True
        print(f"Computer hits! Computer's cards: {cpu1}, current score: {sum(cpu1)}")

    if not cpu_hit:
        print(f"Computer stands! Computer's cards: {cpu1}, current score: {sum(cpu1)}")

    # so, who won?
    print()
    if sum(cpu1) > 21:
        print("CPU bust! You win!")
    elif sum(player1) > sum(cpu1):
        print("You won!")
    elif sum(player1) == sum(cpu1):
        print("Draw!")
    else:
        print("You lose!")


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

