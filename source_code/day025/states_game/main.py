import turtle
import pandas
from writer import Writer

# Initial screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_guessed = []
data = pandas.read_csv('50_states.csv')

# Game code
game_on = True
while game_on:
	answer = screen.textinput(title=f'{len(states_guessed)}/50 States Correct', prompt='Enter a U.S. State:')
	# Try to get the user answer, but if the user immediately cancels with input, break the loop instead of crashing
	try:
		answer = answer.title()
	except AttributeError:
		break
	# If answer hasn't been guessed and it is a state, get the state location info; print it to the map
	if answer not in states_guessed:
		if answer in data['state'].to_list():
			state_row = data[data.state == answer].squeeze()
			# print(state_row)
			state_name = state_row['state']
			x = state_row['x']
			y = state_row['y']
			states_guessed.append(state_name)
			write = Writer()
			write.write_state(state_name, x, y)
	# Continue if user guesses something twice
	elif answer in states_guessed:
		continue
	# Print winning message if user guesses all state correctly
	if len(states_guessed) >= 50:
		write.win_message()
		game_on = False

# States to Learn
missed_states_dict = {
	'missed_states': []
}

# Add each missed state to the dictionary, start DataFrame Index at 1 instead of 0, output to csv
if len(states_guessed) < 50:
	missed_states_dict['missed_states'] = [state for state in data.state.to_list() if state not in states_guessed]
	missed_states = pandas.DataFrame(missed_states_dict)
	missed_states.index += 1
	missed_states.to_csv('missed_states.csv')