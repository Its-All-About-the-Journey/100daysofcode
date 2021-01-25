from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
HEADING = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(HEADING)
        self.player_reset()

    def player_move(self):
        self.forward(MOVE_DISTANCE)

    def player_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def player_reset(self):
        self.goto(STARTING_POSITION)

