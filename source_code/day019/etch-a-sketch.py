from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_back():
    tim.back(10)

def turn_left():
    tim.left(10)
    
def turn_right():
    tim.right(10)

def reset():
    tim.reset()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=reset)
screen.listen()
screen.exitonclick()