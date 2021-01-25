from turtle import Turtle


class Scoreboard(Turtle):

    FONT = ("Courier", 24, "normal")

    def __init__(self, position: tuple, level: int = 1) -> None:
        super().__init__()
        self.level = level
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(position)
        self.refresh()

    def level_up(self) -> None:
        self.level += 1

    def refresh(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=self.FONT)
