from turtle import Turtle
import time


class Ball(Turtle):
	def __init__(self ):
		super().__init__()
		self.y_ball_speed = 3
		self.x_ball_speed = 3
		self.score = (0, 0)
		self.shape('circle')
		self.color('white')
		self.goto(0, 0)
		self.penup()

	def start_move(self):
		time.sleep(0.01)
		new_x = self.xcor() + self.x_ball_speed
		new_y = self.ycor() + self.y_ball_speed
		self.goto(new_x, new_y)

	def collision(self, r_pad, l_pad):
		if (self.distance(r_pad) <= 50 or self.distance(l_pad) <= 50) and abs(self.xcor()) > 340:
			return True

	def check_out_of_bounds(self):
		if self.xcor() < -420:
			return False
		elif self.xcor() > 420:
			return True

	def reverse_y(self):
		self.y_ball_speed = -self.y_ball_speed

	def reverse_x(self):
		self.x_ball_speed = -self.x_ball_speed

	def reset_position(self):
		self.goto(0, 0)
		self.reverse_x()
