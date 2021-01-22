from turtle import Turtle, Screen
import random
import colorgram

t = Turtle()
screen = Screen()
t.shape("turtle")
screen.colormode(255)
screen.bgcolor("white")

colors = colorgram.extract('image.jpg', 30)
rgb_colors = [color.rgb for color in colors]



# def random_walk():
# 	t.shape("circle")
# 	t.hideturtle()
# 	t.speed(20)
# 	t.pensize(15)
# 	move_size = 30
# 	for _ in range(200):
# 		t.pencolor(random.choice(rgb_colors))
# 		turn_angle = random.choice([0, 90, 180, 270])
# 		if turn_angle == 270:
# 			t.left(90)
# 		else:
# 			t.right(turn_angle)
# 		t.forward(move_size)
#
# random_walk()