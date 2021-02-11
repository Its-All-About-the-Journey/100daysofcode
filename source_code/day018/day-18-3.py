import turtle
import random

turtle.colormode(255)

tim = turtle.Turtle()

for i in range(8):
    sides = i + 3
    tim.pencolor(random.randint(1,256),random.randint(1,256),random.randint(1,256))
    for _ in range(sides):
        angle = (360 / sides)
        tim.forward(100)
        tim.right(angle)

screen = turtle.Screen()
screen.exitonclick()