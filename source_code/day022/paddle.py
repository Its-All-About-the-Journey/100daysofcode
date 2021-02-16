from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(starting_position,0)

    def up(self):
        if self.ycor() < 250:
            self.forward(20)

    def down(self):
        if self.ycor() > -235:
            self.back(20)