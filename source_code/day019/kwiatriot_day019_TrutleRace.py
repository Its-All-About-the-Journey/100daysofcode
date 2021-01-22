"""
Day 019 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/21/2021
"""

import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-120, -80, -30, 30, 80, 120]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
