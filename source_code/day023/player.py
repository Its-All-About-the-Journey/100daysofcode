from turtle import Turtle


class Player(Turtle):

    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280

    def __init__(self, home_position: tuple, heading: int = 90) -> None:
        super().__init__()
        self.home_position = home_position
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(heading)
        self.setposition(home_position)

    def move_up(self) -> None:
        self.forward(self.MOVE_DISTANCE)

    def reset(self) -> None:
        self.setposition(self.home_position)
