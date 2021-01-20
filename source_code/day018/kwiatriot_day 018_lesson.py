"""
Day 018 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/19/2021
"""

import turtle as t
import random

wayne = t.Turtle()
wayne.shape("turtle")
t.colormode(255)

# Draw a square with turtle
# for _ in range(4):
#     wayne.forward(100)
#     wayne.right(90)
#
# wayne.left(90)
#
# Draw a dashed line with turtle
# for _ in range(15):
#     wayne.forward(10)
#     wayne.penup()
#     wayne.forward(10)
#     wayne.pendown()

# Draw overlapping shapes with sides 3-10 with random color from a list
# colors = ["CadetBlue", "coral", "DarkRed", "DeepPink", "DodgerBlue", "green"]

# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         wayne.forward(100)
#         wayne.right(angle)
#
# for shape_side_n in range(3, 11):
#     wayne.color(random.choice(colors))
#     draw_shape(shape_side_n)


# Draw a random Walk pattern with a totally random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# heading = [0, 90, 180, 270]
# wayne.pensize(10)
# wayne.speed("fast")
#
# for _ in range(200):
#     wayne.setheading(random.choice(heading))
#     wayne.color(random_color())
#     wayne.forward(20)

# Draw a Spirograph with random colors
def spirograph(shift_angle):
    for _ in range(int(360 / shift_angle)):
        wayne.circle(100)
        wayne.color(random_color())
        wayne.setheading(wayne.heading() + shift_angle)


wayne.speed("fastest")
spirograph(5)

screen = t.Screen()
screen.exitonclick()
