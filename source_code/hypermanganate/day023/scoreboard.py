# 100 Day of Code: Python
# Not Frogger: Main Game
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, pos_x: float, pos_y: float,
                 visible: bool = False) -> None:
        super().__init__(visible=visible)
        self.pu()
        self.setpos(pos_x, pos_y)
        self.score = 1
        self.draw()

    def draw(self):
        self.write(f"Level: {self.score}", font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.draw()

    def end_game(self):
        self.home()
        self.write("Game Over", font=FONT)
