from turtle import Turtle


class ScoreBoard(Turtle):
	SCORE_FONT = ("Comic Sans MS", 16, 'bold')
	LOSS_FONT = ("Comic Sans MS", 24, 'bold')

	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.score = [0, 0]
		self.goto(0, 270)
		self.color('white')
		self.write(f'{self.score[0]} - Score - {self.score[1]}', align='center', font=ScoreBoard.SCORE_FONT)

	def update_p1_score(self):
		self.clear()
		self.score[0] += 1
		self.write(f'{self.score[0]} - Score - {self.score[1]}', align='center', font=ScoreBoard.SCORE_FONT)

	def update_p2_score(self):
		self.clear()
		self.score[1] += 1
		self.write(f'{self.score[0]} - Score - {self.score[1]}', align='center', font=ScoreBoard.SCORE_FONT)

	def game_over(self):
		if self.score[0] == 2:
			self.clear()
			self.goto(0, 0)
			self.write('Player 1 Wins.', align='center', font=ScoreBoard.LOSS_FONT)
			return True
		elif self.score[1] == 2:
			self.clear()
			self.goto(0, 0)
			self.write('Player 2 Wins.', align='center', font=ScoreBoard.LOSS_FONT)
			return True