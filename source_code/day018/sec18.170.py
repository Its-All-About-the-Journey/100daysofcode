from random import choice, randint
import turtle as t

def random_color() -> tuple:
    return randint(0,255), randint(0,255), randint(0,255)

if __name__ == "__main__":
    turtle = t.Turtle()
    turtle.shape("turtle")
    turtle.color("DarkGreen")
    #turtle.pensize(2)
    turtle.speed(80)
    t.colormode(255)

    view = t.Screen()
    view.bgcolor("black")

    radius = 150
    distance = 30
    max_moves = 130
    angle = 3.1
 
    for _ in range(max_moves):
        turtle.pencolor(random_color())
        turtle.circle(radius)
        turtle.left(angle)

    input("Press enter to quit")