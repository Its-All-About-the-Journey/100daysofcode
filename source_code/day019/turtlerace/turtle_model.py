from random import randint

from turtle import Turtle

class TurtleModel():
    
    def __init__(self, color: str, home: tuple) -> None:
        self.color = color
        self.home = home
        self.turtle = Turtle(shape="turtle")
        self.turtle.color(color)
    
    def clear(self) -> None:
        self.turtle.clear()
    
    def forward(self) -> None:
        self.turtle.forward( randint(1,10) )
    
    def home(self) -> tuple:
        return self.home
    
    def pendown(self) -> None:
        self.turtle.pendown()
    
    def penup(self) -> None:
        self.turtle.penup()
    
    def position(self) -> tuple:
        return self.turtle.position()

    def rehome(self) -> None:
        self.turtle.goto(self.home)