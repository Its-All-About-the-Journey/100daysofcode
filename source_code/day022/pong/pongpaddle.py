from turtle import Turtle

class PongPaddle(Turtle):

    PDL_WIDTH = 20
    PDL_HEIGHT = 100
    PDL_MOVE_STEP = 20

    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.setup(position)

    def move_down(self) -> None:
        x, y = self.position()
        self.setposition(x, y - self.PDL_MOVE_STEP)

    def move_up(self) -> None:
        x, y = self.position()
        self.setposition(x, y + self.PDL_MOVE_STEP)

    def setup(self, position: tuple) -> None:
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition((position[0], position[1]))