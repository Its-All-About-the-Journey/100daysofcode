from turtle import Turtle
import time


class Snake:
	MOVE_DISTANCE = 20
	STARTING_SIZE = 5
	RIGHT, UP, LEFT, DOWN = 0, 90, 180, 270

	def __init__(self):
		self.segments = []
		self.initialize_snake()
		self.head = self.segments[0]

	# Initialize the starting snake with a specific starting length
	def initialize_snake(self):
		x, y = 0, 0
		for _ in range(Snake.STARTING_SIZE):
			t = Turtle(shape='square')
			t.penup()
			t.color('white')
			t.goto(x, y)
			x -= 20
			self.segments.append(t)

	# Cause the segments to follow one another
	def move_segments(self):
		time.sleep(0.1)
		for i in range(len(self.segments) - 1, 0, -1):
			self.segments[i].goto(self.segments[i - 1].pos())
		self.segments[0].forward(Snake.MOVE_DISTANCE)

	# Change the heading due north, unless snake is going south
	def up(self):
		if self.head.heading() == Snake.DOWN:
			pass
		else:
			self.head.setheading(Snake.UP)

	# Change the heading due south, unless snake is going north
	def down(self):
		if self.head.heading() == Snake.UP:
			pass
		else:
			self.head.setheading(Snake.DOWN)

	# Change the heading due east, unless snake is going west
	def right(self):
		if self.head.heading() == Snake.LEFT:
			pass
		else:
			self.head.setheading(Snake.RIGHT)

	# Change the heading due west, unless snake is going east
	def left(self):
		if self.head.heading() == Snake.RIGHT:
			pass
		else:
			self.head.setheading(Snake.LEFT)
