# 100 Day of Code: Python
# Not Frogger: Main Game
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self, shape: str = "turtle", undobuffersize: int = 0,
                 visible: bool = True) -> None:
        super().__init__(shape=shape, undobuffersize=undobuffersize,
                         visible=visible)
        self.pu()
        self.setpos(STARTING_POSITION)
        self.seth(90.0)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > STARTING_POSITION[1]:
            self.backward(MOVE_DISTANCE)

    def reset(self):
        self.setpos(STARTING_POSITION)

    def has_reached_goal(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
