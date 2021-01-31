# 100 Days of Code: Python
# Day 21: Snake Game Food Class
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, world_width: int, world_height: int) -> None:
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.goto(random.randint(0 - world_width, world_width), random.randint(0 - world_height, world_height))

    def reposition(self, world_width: int, world_height: int):
        self.goto(random.randint(0 - world_width, world_width), random.randint(0 - world_height, world_height))
