# 100 Days of Code : Python
# Pong Game : Pong Paddle 
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_position_x: int, start_position_y: int, board_y: int = None, speed: int = None) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(1, 5, 1)
        self.setheading(90)
        self.pu()
        self.goto(start_position_x, start_position_y)

        if speed:
            self.paddle_speed = speed

        if board_y:
            self.y_val = board_y

    def move_self(self, ball_y:int = None):
        """
        Move paddle along Y axis between bounds

        Specify ball Y axis position to "chase"
        ball otherwise paddle moves dumb.
        """
        if not ball_y:
            # Dumb Movement

            if abs(self.ycor()) < (self.y_val - 50):
                self.forward(self.paddle_speed)
            else:
                self.setheading(360 - self.heading())
                self.forward(self.paddle_speed)

        else:

            if 0 <= self.heading() <= 180:
                # Facing "Up"
                if ball_y >= self.ycor() and self.ycor() < (self.y_val - 50):
                    # Don't move if we go off the map
                    self.forward(self.paddle_speed)
                else:
                    # Turn around and go after it after it's moved away
                    # a few paces to avoid "overlap"
                    if self.ycor() - ball_y > 20:
                        self.setheading(360 - self.heading())
                        self.forward(self.paddle_speed)

            # Yes it will just flip if the ball is at 0
            if 180 <= self.heading() <= 360:
                # Facing "Up"
                if ball_y <= self.ycor() and self.ycor() > (0 - (self.y_val + 50)):
                    # Don't move if we go off the map
                    self.forward(self.paddle_speed)
                else:
                    # Turn around and go after it after it's moved away
                    # a few paces to avoid "overlap"
                    if ball_y - self.ycor() > 20:
                        self.setheading(360 - self.heading())
                        self.forward(self.paddle_speed)


    def move(self, direction):
        """
        Move paddle
        """

        heading = 0 

        if direction == "up":
            heading = 90
        if direction == "down":
            heading = 270

        if heading == 90 and (self.ycor() < (self.y_val - 50)):
            self.setheading(heading)
            self.forward(self.paddle_speed)
        if (heading == 270 and (self.ycor() > (0 - (self.y_val - 50)))):
            self.setheading(heading)
            self.forward(self.paddle_speed)
