from turtle import Turtle


class Paddle(Turtle):
	def __init__(self, start_pos):
		super().__init__()
		self.paddle_speed = 40
		self.shape('square')
		self.color('white')
		self.penup()
		self.goto(start_pos)
		self.shapesize(stretch_wid=5, stretch_len=0.5)

	# Move right paddle up
	def go_up(self):
		new_y = self.ycor() + self.paddle_speed
		self.goto(self.xcor(), new_y)

	# Move right paddle down
	def go_down(self):
		new_y = self.ycor() - self.paddle_speed
		self.goto(self.xcor(), new_y)




