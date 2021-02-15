from turtle import Turtle
import random
SHAPE = "circle"
COLOR = "blue"
SPEED = "fastest"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(COLOR)
        self.speed(SPEED)
        self.goto(random.randint(-280,280), random.randint(-280,280))
        self.refresh()
    
    def refresh(self):
        self.goto(random.randint(-280,280), random.randint(-280,280))