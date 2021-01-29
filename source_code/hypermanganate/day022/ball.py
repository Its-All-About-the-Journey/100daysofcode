# 100 Days of Code: Python
# Pong Game: Game Ball
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle
from random import choice


class Ball(Turtle):
    def __init__(self, ball_speed: float = 20.0, board_y: int = None) -> None:
        super().__init__()
        self.shape("square")
        self.color((255, 255, 255))
        self.pu()
        self.setheading(int(choice(['45', '135', '225', '315'])))
        self.ball_speed = ball_speed
        self.tilt(45)
        if board_y:
            self.board_y = board_y

    def move_ball(self, collide: bool = False):
        """
        Move ball along its path unless it's collided with something.

        In the video, headings and angles were not a concern which removed
        most of the agony surrounding this.

        Instead, based on which "direction" it was going, and how it collided,
        we either add or subtract from the x/y value depending to steer it.

        """
        collide_wall = False

        if abs(self.ycor()) >= self.board_y - 20:
            collide_wall = True

        if collide_wall:
            self.setheading(360 - self.heading())

        if collide:
            if self.heading() in [135.0, 315.0]:
                self.setheading(self.heading() - 90)
            elif self.heading() in [45.0, 225.0]:
                self.setheading(self.heading() + 90)
            else:
                print("Bad angle")

        self.forward(self.ball_speed)

    def reset(self, direction: str = None):
        """
        Return ball to home, and select a new angle to start from.

        If specfiying a start direction, left or right,
        angles are limited to those directions.

        """

        angles = []

        if not direction or direction == "left":
            angles += ['135', '225']
        if not direction or direction == "right":
            angles += ['45', '315']

        self.home()
        self.setheading(int(choice(angles)))
