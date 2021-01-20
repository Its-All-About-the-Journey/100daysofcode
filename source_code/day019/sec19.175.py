from turtle import Turtle, Screen



def move_forward():
    tim.forward(10)

def init():
    view.listen()
    view.onkey(key="space", fun=move_forward)

if __name__ == "__main__":
    view = Screen()
    tim = Turtle()

    init()
    view.exitonclick()
