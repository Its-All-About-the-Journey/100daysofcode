import pandas
import turtle

IMAGE_FILE = "./states/blank_states_img.gif"
STATES_FILE = "./states/50_states.csv"
FILENAME_OUT = "./states/states_to_learn.csv"

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("U.S. State Game")
    image = IMAGE_FILE
    screen.addshape(image)
    turtle.shape(image)

    # Load states
    data = pandas.read_csv(STATES_FILE)
    states = data.state.to_list()
    state_position = [pos for pos in zip(data.x.to_list(), data.y.to_list())]
    num_of_states = len(states)

    correct_guesses = list()

    while len(correct_guesses) != num_of_states:
        guess = screen.textinput(
            title=f"{len(correct_guesses)}/{num_of_states}Guess the State",
            prompt="What's another state's name"
        )

        # Player can cancel with "cancel" button or typing "exit"
        if not guess or guess == "exit":
            break

        guess = guess.title()

        if guess in correct_guesses:
            continue

        # Write state on map, if not already guessed
        if guess in states:
            state_label = turtle.Turtle()
            state_label.hideturtle()
            state_label.penup()

            # Get location
            state_data = data[data.state == guess]
            state_label.setposition((int(state_data.x), int(state_data.y)))
            state_label.write(guess)

            # Add to correct guesses list
            correct_guesses.append(guess)

    # Get difference of states - guessed states, and sort the set
    states_not_guessed = sorted(set(states) - set(correct_guesses))

    # Write to file the non-guessed states
    data_out = pandas.DataFrame(states_not_guessed)
    data_out.to_csv(FILENAME_OUT)
