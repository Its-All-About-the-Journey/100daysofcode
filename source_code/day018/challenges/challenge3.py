from turtle import Turtle, Screen
import random

tim = Turtle()

# drawing the square
# for t in range(50):
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

screen = Screen()
screen.colormode(255)

def shape_color():
    tup = ()
    for c in range(3):
        color = random.randint(1, 256)
        tup += (color,)
    return tup

def draw_shapes(shape_size):
    angle = 360 / shape_size
    for x in range(shape_size):
        tim.forward(100)
        tim.right(angle)

for shape_size in range(3, 11):
    tim.color(shape_color())
    draw_shapes(shape_size)


screen.exitonclick()
