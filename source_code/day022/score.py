from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 32, "normal")
COLOR = "white"

class Score(Turtle):
    def __init__(self, player):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-60 if player == "player1" else 60, 250)
        self.color(COLOR)
        self.update_scoreboard(player)

    def update_scoreboard(self, player):
        self.clear()
        self.goto(-60 if player == "player1" else 60, 250)
        self.write(f"{self.score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self, player):
        self.score += 1
        self.update_scoreboard(player)