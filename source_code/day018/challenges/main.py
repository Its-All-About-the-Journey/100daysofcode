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

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    col_tup = (r, g, b)
    return col_tup

#tim.pensize(10)
tim.speed("fastest")

for x in range(1,121):
    tim.color(random_color())
    tim.circle(100)
    tim.right(3)

screen.exitonclick()
