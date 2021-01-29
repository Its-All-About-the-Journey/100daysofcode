from turtle import Turtle
from random import randint
from rgb import random_rgb_light


class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape('circle')
		self.penup()
		self.shapesize(0.5, 0.5)
		self.color(random_rgb_light())
		self.speed('fastest')
		random_x, random_y = randint(-280, 280), randint(-280, 280)
		self.goto(random_x, random_y)