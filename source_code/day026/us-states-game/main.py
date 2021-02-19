import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725,height=491)
image = "source_code/day026/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("source_code/day026/us-states-game/50_states.csv")
remaining_states = pandas.read_csv("source_code/day026/us-states-game/remaining_states.csv")
all_states = states.state.tolist()
guesses = []

def populate_guesses():
    for state in all_states:
        if state not in remaining_states.state.tolist():
            state_text = turtle.Turtle()
            state_text.hideturtle()
            state_text.penup()
            state_text.goto(int(states.x[states.state == state]), int(states.y[states.state == state]))
            state_text.write(f"{state}", True, align="center", font=("Calibri", 8, "normal"))
            guesses.append(state)

def guess(x, y):
    guess = screen.textinput(f"{len(guesses)}/{len(states.state.tolist())} States Correct", "Which state do you think it is?: ").title()
    if guess == "Exit":
        remaining_states = [state for state in all_states if state not in guesses]
        remaining_states = pandas.DataFrame(remaining_states)
        remaining_states.to_csv("source_code/day026/us-states-game/remaining_states.csv")
        exit()
    elif guess in all_states and int(states.x[states.state == guess]) > x-70 and int(states.x[states.state == guess]) < x+70 and int(states.y[states.state == guess]) > y-70 and int(states.y[states.state == guess]) < y+70:
        state_text = turtle.Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_text.goto(int(states.x[states.state == guess]), int(states.y[states.state == guess]))
        state_text.write(f"{guess}", True, align="center", font=("Calibri", 8, "normal"))
        guesses.append(guess)
        check_for_win()

def check_for_win():
    if len(guesses) == len(all_states):
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.color("purple")
        game_over.goto(0,0)
        game_over.write(f"You guessed them all!", True, align="center", font=("Calibri", 24, "normal"))
        states.to_csv("source_code/day026/us-states-game/remaining_states.csv")

populate_guesses()

turtle.onscreenclick(guess)

while len(guesses) < len(all_states):
    turtle.mainloop()