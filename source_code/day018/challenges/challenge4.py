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
    tup = (r, g, b)
    return tup

def random_distance():
    distance = random.randint(30,40)
    return distance

def random_turn():
    turn = random.choice(["right", "left"])
    return turn

tim.pensize(10)
tim.speed("fastest")

for walk in range(1,100):
    tim.color(random_color())
    tim.forward(random_distance())
    #turn = random_turn()
    tim.right(random.randint(0,360))

screen.exitonclick()
