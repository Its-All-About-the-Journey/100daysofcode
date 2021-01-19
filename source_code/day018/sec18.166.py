from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("DarkGreen")

view = Screen()

# Draw a dashed line
alternating_distance = 10

for _ in range(50):
    turtle.penup() if turtle.isdown() else turtle.pendown()
    turtle.forward(alternating_distance)

input("Press enter to quit")