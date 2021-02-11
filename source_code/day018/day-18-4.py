import turtle
import random
turtle.colormode(255)

tim = turtle.Turtle()
tim.speed(10)
tim.pensize(width=10)

heading = [0, 90, 180, 270]

for i in range(200):
    tim.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
    tim.setheading(random.choice(heading))
    tim.forward(30)

screen = turtle.Screen()
screen.exitonclick()