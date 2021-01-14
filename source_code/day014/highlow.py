import os
from random import choice

from art import logo, vs
from game_data import data

# Constants
MSG_DATA_INFO        = "Compare {side}: {name}, {description}, from {country}"
MSG_CORRECT          = "You're right!"
MSG_WRONG            = "Sorry, that's wrong."
MSG_SCORE            = "Current score: {}"
MSG_FINAL_SCORE      = "Your final score was {}"
MSG_WANNA_PLAY_AGAIN = "Do you want to play again? Type 'y' or any key to quit: "
MSG_WANNA_PLAY       = "Do you want to play? Type 'y' or any key to quit: "
MSG_A_OR_B           = "Who has more followers? Type 'A' or 'B': "

def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game() -> int:
    score = 0

    wrong_guess = False

    # Repeat until wrong guess
    while not wrong_guess:
        # Get data for sides a and b
        a, b = get_data_pair(data)

        refresh_screen( 
            [
                logo,
                MSG_DATA_INFO.format(side='A', name=a['name'], description=a['description'], country=a['country']),
                vs,
                MSG_DATA_INFO.format(side='B', name=b['name'], description=b['description'], country=b['country']),
                MSG_SCORE.format(score)
            ]
        )

        print()
        guess = input(MSG_A_OR_B)[0]

        # Calculate followers from A's point of view
        followers_a_pov = a['follower_count'] - b['follower_count']

        if followers_a_pov < 0 and guess == 'B':  # Player chose B: A < B
            score += 1

        elif followers_a_pov  and guess == 'A':   # Player chose A: A > B
            score += 1

        else: # Player chose wrong side or both sides are equal
            wrong_guess = True
            refresh_screen([logo, MSG_WRONG])

    return score

def refresh_screen(msgs: list) -> None:
    clear()

    for msg in msgs:
        print(msg)

def get_data_pair(data: list) -> tuple:
    a = choice(data)
    b = choice(data)

    while a == b:
        b = choice(data)

    return a,b

def run_game():
    '''
    Asks user if they want to play
    '''

    quit = input(MSG_WANNA_PLAY)[0]  != 'y'

    while not quit:

        score = play_game()

        print( MSG_FINAL_SCORE.format(score) )
        print()

        quit = input(MSG_WANNA_PLAY_AGAIN) != 'y'


if __name__ == '__main__':

    run_game()
