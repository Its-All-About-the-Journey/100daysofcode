import turtle
import random
turtle.colormode(255)

tim = turtle.Turtle()
tim.speed(10)

def draw_spiro(gap):
    for _ in range(int(360 / gap)):
        tim.setheading(tim.heading() + gap)
        tim.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        tim.circle(100)

draw_spiro(int(input("How far apart should the circles be?: ")))
screen = turtle.Screen()
screen.exitonclick()