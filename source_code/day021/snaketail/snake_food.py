import random
from turtle import Turtle

class SnakeFood(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("green")
        self.speed("fastest")
        self.respawn()
    
    def respawn(self) -> None:
        self.goto(random.randint(-280, 280), random.randint(-280, 280))