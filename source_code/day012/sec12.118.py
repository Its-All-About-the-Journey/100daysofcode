import constants as CONST
from random import randint

from util import refresh_screen

def init_game():
    refresh_screen( [CONST.LOGO, CONST.MSG_WELCOME] )

def new_game_setup():
    refresh_screen( [CONST.LOGO, CONST.MSG_GUESS_RANGE, CONST.MSG_CHOOSE_DIFFICULTY] )

    difficulty = input().lower()[0]

    if difficulty == 'e':
        tries = 10
    elif difficulty == 'h':
        tries = 5
    else:
        tries = 1
    
    number = randint(1,100)

    return number, tries

def make_guess(attempts_left):
    #refresh_screen( [CONST.LOGO, CONST.MSG_ATTEMPTS_LEFT.format(attempts_left), CONST.MSG_MAKE_GUESS] )
    print()
    print( CONST.MSG_ATTEMPTS_LEFT.format(attempts_left) )
    return int( input(CONST.MSG_MAKE_GUESS) )

def run_game():
    is_game_over = False

    while not is_game_over:
        # Setup game
        number, attempts_left = new_game_setup()

        # Guess number until it matches or run out of tries
        while attempts_left:
            
            guess = make_guess(attempts_left)
            attempts_left -= 1

            # Is guess too low, too high, or exact
            result = number - guess

            if not result:
                # Guessed correctly
                attempts_left = 0
            
            elif result > 0:
                # Too low
                refresh_screen( [CONST.LOGO, CONST.MSG_GUESS_TOO_LOW, CONST.MSG_GUESS_AGAIN] )
            else:
                # Too high
                refresh_screen( [CONST.LOGO, CONST.MSG_GUESS_TOO_HIGH, CONST.MSG_GUESS_AGAIN] )


        # Print results
        if number == guess:
            refresh_screen( [CONST.LOGO, CONST.MSG_YOU_WIN] )
        else:
            refresh_screen( [CONST.LOGO, CONST.MSG_YOU_LOSE, CONST.MSG_ANSWER.format(number)] )

        # Does the player want to continue or quit
        print()
        is_game_over = False if input(CONST.MSG_PLAY_AGAIN)[0] == 'y' else True

if __name__ == '__main__':

    # Print intial game messages and then run game
    init_game()
    run_game()
    