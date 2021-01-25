from turtle import Turtle

class PongBall(Turtle):
    
    DEFAULT_SPEED = 0.1

    def __init__(self) -> None:
        super().__init__()
        self.ball_x_step = 10
        self.ball_y_step = 10
        self.move_speed = 0.1
        self.move_speed_multiplier = 0.9
        self.start_position = 0, 0
        self.setup()
    
    def bounce_x(self) -> None:
        self.ball_x_step *= -1
        self.move_speed *= self.move_speed_multiplier

    def bounce_y(self) -> None:
        self.ball_y_step *= -1

    def move(self) -> None:
        x,y = self.position()
        self.setposition( x + self.ball_x_step, y + self.ball_y_step )

    def reset_position(self) -> None:
        self.setposition(self.start_position)
        self.move_speed = self.DEFAULT_SPEED
        self.bounce_x()

    def setup(self) -> None:
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setposition(self.start_position)