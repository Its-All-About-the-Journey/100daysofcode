"""
Day 019 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/21/2021
"""

import turtle as t

tim = t.Turtle()
screen = t.Screen()

# Creating an Etch-a-sketch program
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clock():
    tim.left(5)

def move_clock():
    tim.right(5)

def clear():
    tim.penup()
    tim.clear()
    tim.setpos(0, 0)
    tim.setheading(0)
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
