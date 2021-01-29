# 100 Days of Code: Python
# Pong Game: Scoreboard Class
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle

FONT_SIZE = 80


class Scoreboard(Turtle):
    def __init__(self, world_height: int, world_width: int) -> None:
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color((255, 255, 255))
        self.goto(0, world_height / 2 - (FONT_SIZE + 40))

        self.player_score = 0
        self.computer_score = 0

        self.draw_score()

    def add_point_player(self):
        self.player_score += 1
        self.draw_score()

    def add_point_computer(self):
        self.computer_score += 1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.write(f"{self.player_score}    {self.computer_score}", align="center", font=("Courier", FONT_SIZE, "normal"))

    def end_game(self, win: bool = False):
        """
        End the game.

        Specify 'win' if the player has won.
        """
        self.goto(0, 20)
        self.write("Game Over", align="center", font=("Calabri", "14", "bold"))
        self.goto(0, -20)
        message = "Try Again!"
        if win:
            message = "You Win!"
        self.write(message, align="center", font=("Calabri", "14", "bold"))
