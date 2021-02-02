from turtle import Turtle
import os


class ScoreBoard(Turtle):
	SCORE_FONT = ("Comic Sans MS", 12, 'bold')
	LOSS_FONT = ("Comic Sans MS", 24, 'bold')

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.score = 0
		if not os.path.exists('data.txt'):
			with open('data.txt', 'w') as f:
				f.write('0')
		with open('data.txt', 'r') as f:
				self.high_score = int(f.read())
		self.goto(0, 280)
		self.color('white')
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=ScoreBoard.SCORE_FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			with open('data.txt', 'w') as f:
				f.write(str(self.high_score))
		self.score = 0
		self.update_score()

	def increase_score(self):
		self.score += 1
		self.update_score()

	# def game_over(self):
	# 	self.goto(0, 0)
	# 	self.write('Game Over.', align='center', font=ScoreBoard.LOSS_FONT)

