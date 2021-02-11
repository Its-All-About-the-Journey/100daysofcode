import colorgram
import turtle
import random

turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('source_code\\day018\\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

tim = turtle.Turtle()
tim.hideturtle()
tim.speed(10)
tim.penup()
tim.goto(-250,-250)

def paint_row():
    for i in range (0,10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)

def reset_row():
    tim.back(500)
    tim.left(90)
    tim.forward(50)
    tim.right(90)

for i in range (0,10):
    paint_row()
    reset_row() 

screen = turtle.Screen()
screen.exitonclick()