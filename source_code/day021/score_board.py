from turtle import Turtle


class ScoreBoard(Turtle):
	SCORE_FONT = ("Comic Sans MS", 12, 'bold')
	LOSS_FONT = ("Comic Sans MS", 24, 'bold')

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.score = 0
		self.goto(0, 280)
		self.color('white')
		self.write(f'Score: {self.score}', align='center', font=ScoreBoard.SCORE_FONT)

	def update_score(self):
		self.clear()
		self.score += 1
		self.write(f'Score: {self.score}', align='center', font=ScoreBoard.SCORE_FONT)

	def game_over(self):
		self.goto(0, 0)
		self.write('Game Over.', align='center', font=ScoreBoard.LOSS_FONT)
