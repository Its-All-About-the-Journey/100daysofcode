from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=600)

is_racing = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
all_turtles = []


for x in range(0, len(colors)):
    name = colors[x]
    name = Turtle(shape = "turtle")
    name.color(colors[x])
    name.penup()
    name.speed(speed="fastest")
    x_coord = -230
    y_coord = (x * 100) - 250
    name.goto(x = x_coord, y = y_coord)
    all_turtles.append(name)

if user_bet:
    is_racing = True

while is_racing:
    for t in all_turtles:
        if t.xcor() >= 230:
            winner = t
            is_racing = False
        else:
            dist = random.randint(1, 10)
            t.forward(dist)

if user_bet == winner.pencolor():
    print(f"The winner is {winner.pencolor().capitalize()}! Well done!")
else:
    print(f"{winner.pencolor().capitalize()} won the race, better luck next time!")

screen.exitonclick()