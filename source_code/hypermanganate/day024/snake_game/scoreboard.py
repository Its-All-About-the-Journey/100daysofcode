# 100 Days of Code: Python
# Snake Game: Scoreboard Class
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, world_height: int, world_width: int) -> None:
        super().__init__()
        self.pu()
        self.high_score = 0
        self.score = -1
        self.hideturtle()
        self.color((255, 255, 255))
        self.goto(0, world_height / 2 - 30)
        self.add_point()
        with open("high_score") as file:
            self.high_score = int(file.read())

    def add_point(self):
        self.clear()
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"Snake Game - Score {self.score} (High: {self.high_score})", align="center", font=("Calabri", "14", "bold"))

    def end_game(self):
        self.goto(0, 20)
        self.write("Game Over", align="center", font=("Calabri", "14", "bold"))
        self.goto(0, -20)
        self.write("Snake Has Died", align="center", font=("Calabri", "14", "bold"))

    def reset(self):
        with open("high_score", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = -1
        self.add_point()
