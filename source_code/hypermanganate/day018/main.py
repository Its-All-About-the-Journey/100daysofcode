#!/usr/bin/env python3
# 100 Days of Code : Python
# Day 18 : Hirst Painting
# Adam Pawlowski @hypermanganate


from turtle import Turtle, Screen
from random import randint
from colorgram import extract

NUM_COLORS = 35
DIMENSION = 80
DOT_SIZE = 10
SPACER = 5
PHOTO = 'beeraisle.pg'


def gimme_rgb():
    """
    Return the RGB color value of a random color in the pallette
    """
    color = colors[randint(0, len(colors) - 1)]
    rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    return rgb_tuple


def setup_turtle():
    """
    Setup Turtle Parameters and return Turtle object
    """
    turtle = Turtle()
    turtle.shape("classic")
    turtle.penup()
    turtle.seth(0)
    turtle.speed(0)

    return turtle


def setup_screen():
    """
    Setup Screen Parameters and return Screen object
    """
    screen = Screen()
    screen.colormode(255)

    return screen


def draw_frame(turtle):
    """
    Draw some sort of border with bad math around the art
    """
    side_len = (DIMENSION // DOT_SIZE) * (DOT_SIZE * SPACER)
    turtle.pencolor(200, 50, 100)
    turtle.setpos(0 - (DOT_SIZE + 2 * SPACER), 0 - (DOT_SIZE + 2 * SPACER))
    turtle.seth(0)
    turtle.pendown()
    for _ in range(4):
        turtle.fd(side_len)
        turtle.left(90)
    turtle.penup()


num_dots = DIMENSION // DOT_SIZE

my_turtle = setup_turtle()
my_screen = setup_screen()
colors = extract('./beeraisle.png', NUM_COLORS)

my_turtle.home()

for row in range(num_dots):
    print(f"Row {row}")
    my_turtle.setpos(0, (DOT_SIZE * row * SPACER))
    for _ in range(num_dots):
        my_turtle.dot(DOT_SIZE, gimme_rgb())
        my_turtle.forward(DOT_SIZE * SPACER)

draw_frame(my_turtle)

my_screen.exitonclick()
