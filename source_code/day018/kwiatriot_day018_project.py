"""
Day 018 of the 100 Days of Code course
Author: Wayne Kwiat
Date: 1/19/2021
"""
import turtle as t
import random
# import colorgram
#
# Using the colorgram module to generate the color list
# colors = colorgram.extract('DH_spot.jpeg', 30)
#
# rgb_list = []
#
# for item in colors:
#     r = item.rgb.r
#     g = item.rgb.g
#     b = item.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
#
# print(rgb_list)

t.colormode(255)
wayne = t.Turtle()
screen = t.Screen()
wayne.speed("fastest")
color_list = [(240, 234, 83), (209, 159, 99), (185, 11, 67), (114, 177, 205), (26, 115, 166), (217, 131, 165), (173, 170, 30), (167, 78, 34), (131, 185, 147), (223, 60, 105), (10, 28, 72), (176, 48, 96), (34, 134, 80), (235, 76, 44), (234, 229, 4), (234, 164, 192), (78, 11, 59), (11, 49, 29), (25, 167, 209), (19, 43, 131), (58, 167, 100), (11, 100, 60), (134, 214, 228), (84, 25, 11), (135, 32, 20), (161, 211, 176)]

wayne.penup()
wayne.ht()
wayne.setpos(-230, -230)
num_dots = 100

for dots in range(1, num_dots + 1):
    wayne.dot(20, random.choice(color_list))
    wayne.forward(50)

    if dots % 10 == 0:
        wayne.setheading(90)
        wayne.forward(50)
        wayne.setheading(180)
        wayne.forward(500)
        wayne.setheading(0)

screen.exitonclick()
