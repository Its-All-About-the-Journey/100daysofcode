from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.can_be_hit = True
        self.goto(0,0)
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.penup()
        self.speed("fast")
        self.timer = .1
        self.xmove = 10
        self.ymove = 10

    def move(self):
        self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)

    def bounce(self):
        self.ymove *= -1
    
    def hit(self):
        if self.can_be_hit == True:
            self.xmove *= -1
            self.timer /= 1.1

    def reset(self):
        self.can_be_hit = True
        self.goto(0,0)
        self.timer = .1
        self.hit()