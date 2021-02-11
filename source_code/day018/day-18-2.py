from turtle import Turtle
from turtle import Screen

#timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")

square = Turtle()
for _ in range(50):
    square.forward(10)
    square.penup()
    square.forward(10)
    square.pendown()











screen = Screen()
screen.exitonclick()