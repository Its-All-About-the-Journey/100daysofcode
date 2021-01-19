from random import choice, randint
import turtle as t

def draw_random(angle: int, distance: int, turtle: t.Turtle) -> None:
    turtle.forward(distance)
    turtle.left(angle)

def random_color() -> tuple:
    return randint(0,255), randint(0,255), randint(0,255)

if __name__ == "__main__":
    turtle = t.Turtle()
    turtle.shape("turtle")
    turtle.color("DarkGreen")
    turtle.pensize(7)
    turtle.speed(80)
    t.colormode(255)

    view = t.Screen()
    view.bgcolor("black")

    distance = 30
    max_moves = 100

    angles = [0, 90, 180, 270]
 
    for _ in range(max_moves):
        turtle.pencolor(random_color())
        angle = choice(angles)
        draw_random(angle, distance, turtle)

    input("Press enter to quit")