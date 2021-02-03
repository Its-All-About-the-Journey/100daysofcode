from turtle import Turtle


class Writer(Turtle):
	FONT_1 = ("Comic Sans MS", 8, 'bold')
	FONT_2 = ("Comic Sans MS", 24, 'bold')

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.speed('fastest')
		self.color('black')

	def write_state(self, state, x, y):
		self.goto(x, y)
		self.write(f'{state}', font=Writer.FONT_1)

	def win_message(self):
		self.color('blue')
		self.goto(-300, -250)
		self.write("You've guessed all 50 states! Congrats!", font=Writer.FONT_2)
