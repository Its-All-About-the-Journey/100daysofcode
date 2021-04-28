from turtle import Turtle, Screen
import random

dotgen = Turtle()

screen = Screen()
screen.colormode(255)

color_list = [(238, 239, 240), (238, 238, 235), (232, 236, 233), (241, 234, 238), (41, 104, 174), (234, 205, 114), (228, 151, 85), (189, 46, 74), (231, 118, 144), (115, 90, 46), (110, 107, 189), (216, 60, 77), (114, 186, 136), (122, 176, 212), (52, 178, 110), (204, 16, 40), (115, 171, 36), (223, 57, 47), (31, 58, 117), (154, 223, 195), (182, 168, 223), (23, 142, 107), (29, 164, 172), (85, 35, 37), (39, 45, 84), (229, 169, 182), (232, 174, 161), (81, 39, 38), (151, 206, 223), (92, 43, 42)]

for x in range(1,11):
    y_coord = (x * 25) - 125
    dotgen.penup()
    dotgen.setpos((-125,y_coord))
    for dot in range(1, 11):
        color = random.choice(color_list)
        dotgen.dot(15, color)
        dotgen.penup()
        dotgen.forward(25)

screen.exitonclick()