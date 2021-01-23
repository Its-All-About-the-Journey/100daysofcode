from turtle import Turtle, Screen
import random
import colorgram


# Function to set initial window and turtle settings
def initialize_hirst():
	t = Turtle()
	t.hideturtle()
	t.shape("arrow")
	t.speed('fastest')
	t.penup()
	screen = Screen()
	screen.colormode(255)
	screen.bgcolor("white")
	screen.setup(1100, 1100)
	return t, screen


# Function to get color palette from photo and filter out the lightest colors
def gen_filter_colors():
	colors = colorgram.extract('image.jpg', 30)
	rgb_colors = [color.rgb for color in colors]
	for index, color in enumerate(rgb_colors):
		if color.r > 230 and color.g > 230 and color.b > 230:
			rgb_colors.pop(index)
	return rgb_colors


# Function to paint the 100 dots on the canvas
def paint_hirst():
	t, screen = initialize_hirst()
	colors = gen_filter_colors()
	y_move = 100
	initial_x = -450
	initial_y = -575
	for _ in range(10):
		t.setposition(initial_x, initial_y + y_move)
		y_move += 100
		for _ in range(10):
			color = random.choice(colors)
			t.pencolor(color)
			t.fillcolor(color)
			t.pendown()
			t.begin_fill()
			t.circle(35)
			t.end_fill()
			t.penup()
			t.forward(100)
	screen.exitonclick()


paint_hirst()

