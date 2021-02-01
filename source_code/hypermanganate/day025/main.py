# 100 Days of Code: Python
# 50 States Game
# Adam Pawlowski (@hypermanganate)

from turtle import Screen, Turtle
import pandas
from pandas.core.series import Series

my_screen = Screen()
my_screen.screensize(725, 491)
my_screen.bgpic("./blank_states_img.gif")
my_screen.title("Merica Map")

state_data = pandas.read_csv("./50_states.csv")
score = 0
total_number_of_states = len(state_data)


def write_state(state_data: Series):
    label = Turtle(visible=False)
    label.pu()
    label.goto(float(state_data.x), float(state_data.y))
    label.write(state_data.state.to_string(index=False))


while len(state_data) > 0:
    number_of_states_remaining = len(state_data)

    print(f"There are {number_of_states_remaining} states to guess.")
    my_screen.title(f"Merica Map - {number_of_states_remaining}" +
                    " States Remaining")
    guess = my_screen.textinput(
        f"Your Guess ({score}/{total_number_of_states} Guessed)",
        prompt="Your Guess (exit to quit)"
        )
    guess = guess.title()
    if guess == "Exit":
        break
    if state_data[state_data.state == guess].empty:
        pass
    else:
        write_state(state_data[state_data.state == guess])
        state_data.drop(
            state_data[state_data.state == guess].index,
            inplace=True
            )
        score += 1

if len(state_data):
    print(f"There were {len(state_data)} states remaining.")
    state_data.to_csv("./states_to_learn.csv")
