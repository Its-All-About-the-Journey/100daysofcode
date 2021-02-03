import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_guessed = []
data = pandas.read_csv('50_states.csv')

game_on = True
while game_on:
	answer = screen.textinput(title=f'{len(states_guessed)}/50 States Correct', prompt='Enter a U.S. State:')
	answer = answer.title()
	if answer not in states_guessed:
		if answer in data['state'].to_list():
			state_row = data[data.state == answer].squeeze()
			print(state_row)
			state_name = state_row['state']
			x = state_row['x']
			y = state_row['y']
			states_guessed.append(state_name)
			write = Writer()
			write.write_state(state_name, x, y)
	elif answer in states_guessed:
		continue
	if len(states_guessed) >= 50:
		game_on = False

write.win_message()

turtle.mainloop()