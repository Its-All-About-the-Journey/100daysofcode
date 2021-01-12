import os
import random

from art import logo

DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

MSG_WANNA_PLAY = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
MSG_PLAYER_CARDS = "Your cards: {}, current score: {}"
MSG_CPU_CARDS = "Computer's first card: {}"
MSG_HIT_OR_STAND = "Type 'y' to get another card, type 'n' to pass: "
MSG_PLALYER_FINAL_SCORE = "Your final hand: {}, final score: {}"
MSG_CPU_FINAL_SCORE = "Computer's final hand: {}, final score {}"
MSG_PLAYER_WON = "You win"
MSG_PLAYER_LOST = "You lost!"
MSG_PLAYER_DRAW = "It's a draw"

# Clear the terminal screen
def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def deal(deck: list) -> int:
    return deck[ random.randint(0, len(deck) - 1 ) ]

def calculate_score(cards: list) -> int:
    ace_count = 0
    score = 0

    for card in cards:
        if card == 11:
            ace_count += 1
        else:
            score += card
    
    for _ in range(ace_count):
        if (score + 11) <= 21:
            score += 11
        else:
            score += 1

    return score

def winning_msg(player_final_score: int, cpu_final_score: int) -> str:
    
    if (player_final_score > 21) or (player_final_score < cpu_final_score):
        msg = MSG_PLAYER_LOST

    elif player_final_score > cpu_final_score:
        msg = MSG_PLAYER_WON
    
    else:
        msg =MSG_PLAYER_DRAW
    
    return msg

def refresh_screen(messages: list) -> None:
    clear()
    print(logo)
    for msg in messages:
        print(msg)

play_game = True

# Game loop
while play_game:
    player_cards = list()
    cpu_cards = list()

    # Deal starting hand
    player_cards.append( deal(DECK) )
    cpu_cards.append( deal(DECK) )
    player_cards.append( deal(DECK) )
    cpu_cards.append( deal(DECK) )

    # Refresh - dealt hand
    refresh_screen(
        [
            MSG_PLAYER_CARDS.format( player_cards, calculate_score(player_cards) ),
            MSG_CPU_CARDS.format(cpu_cards[0])
        ]
    )
    
    # # Player - Hit or Stand
    keep_dealing_player = True

    while keep_dealing_player:
        print()
        player_next_move = input(MSG_HIT_OR_STAND)

        if player_next_move[0] == 'y':
            player_cards.append( deal(DECK) )

            # Refresh - dealt card
            refresh_screen(
                [
                    MSG_PLAYER_CARDS.format( player_cards, calculate_score(player_cards) ),
                    MSG_CPU_CARDS.format(cpu_cards[0])
                ]
            )
        else:
            keep_dealing_player = False  

        player_score = calculate_score(player_cards)

        if player_score > 21:
            keep_dealing_player = False

    # CPU hit or stand
    while (player_score <= 21) and ( calculate_score( cpu_cards ) < 17 ):
        cpu_cards.append( deal(DECK) )

    # Print final hand
    player_final_score = calculate_score(player_cards)
    cpu_final_score = calculate_score(cpu_cards)

    refresh_screen(
        [
            MSG_PLALYER_FINAL_SCORE.format(player_cards, calculate_score(player_cards) ),
            MSG_CPU_FINAL_SCORE.format(cpu_cards, calculate_score(cpu_cards) )
        ]
    )

    print( winning_msg(player_final_score, cpu_final_score) )

    # Does the player want to play again
    print()
    play_game = input(MSG_WANNA_PLAY)

    play_game = False if play_game[0] != 'y' else True