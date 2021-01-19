from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("DarkGreen")

view = Screen()

# Draw a Square
distance = 25
angle = 90

for _ in range(4):
    turtle.forward(distance)
    turtle.left(angle)

input("Press enter to quit")