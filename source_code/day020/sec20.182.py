from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Python Game")

tim = Turtle("circle")
tim.pencolor("green")
tim.pensize(20)

pos_width = 20
positions = [(0,0), (-1,0), (-2,0)]

for pos in positions:
    tim.goto(pos[0] * pos_width, pos[1] * pos_width)

screen.exitonclick()
