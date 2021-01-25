from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.level = 1
        self.goto(280, -280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-290, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def point(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
