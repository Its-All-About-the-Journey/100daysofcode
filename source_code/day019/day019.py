from turtle import Turtle, Screen
import random

s = Screen()
s.setup(500, 400)
user_bet = s.textinput(title="Place Your Bet", prompt="Which turtle will win the race? Enter a color (rainbow colors): ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'indigo']

# Initalize the turtle dictionary
turtles = {}
y_coord = -150
# Loop initializes each turtle and adds it to the dictionary with a key equal to its color - also sets starting coords
for x in range(0, 7):
	turtles[f'{colors[x]}'] = Turtle(shape='turtle')
	turtles[f'{colors[x]}'].penup()
	turtles[f'{colors[x]}'].fillcolor(colors[x])
	turtles[f'{colors[x]}'].goto(x=-230, y=y_coord)
	y_coord += 50

if user_bet:
	start = True

# Loop will move each turtle ahead a random distance and declare winner once one reaches the finish line
while start:
	for key, turtle in turtles.items():
		turtle.forward(random.randint(0, 15))
		if turtle.position()[0] > 230:
			start = False
			if user_bet.lower() == key:
				print(f'You win!!! The {key} turtle is the winner!')
			else:
				print(f'You lose. The {key} turtle is the winner!')

s.exitonclick()
