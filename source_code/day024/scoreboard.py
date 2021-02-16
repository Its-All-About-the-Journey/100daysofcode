from turtle import Turtle, write
ALIGNMENT = "center"
FONT = ("Calibri", 12, "normal")
COLOR = "white"
PATH_TO_SCORE = "source_code/day024/score.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(PATH_TO_SCORE, mode="r+") as score_file:
            self.high_score = int(score_file.read())
        self.hideturtle()
        self.goto(0, 280)
        self.penup()
        self.color(COLOR)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        self.goto(0, 0)
        if self.score > self.high_score:
            with open(PATH_TO_SCORE), mode="w") as score_file:
                score_file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()