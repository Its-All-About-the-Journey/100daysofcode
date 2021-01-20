from random import randint

from turtle import Turtle

class TurtleModel():
    
    def __init__(self, color: str, home: tuple):
        self.color = color
        self.home = home
        self.turtle = Turtle(shape="turtle")
        self.turtle.color(color)
    
    def clear(self):
        self.turtle.clear()
    
    def forward(self):
        self.turtle.forward( randint(1,10) )
    
    def home(self) -> tuple:
        return self.home
    
    def pendown(self):
        self.turtle.pendown()
    
    def penup(self):
        self.turtle.penup()
    
    def position(self) -> tuple:
        return self.turtle.position()

    def rehome(self) -> None:
        self.turtle.goto(self.home)