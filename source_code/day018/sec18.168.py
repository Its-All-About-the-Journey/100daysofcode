import random
from turtle import Turtle, Screen

def draw_random(angle: int, distance: int, color: str, turtle: Turtle, speed: int, pensize: int) -> None:
    turtle.pencolor(color)
    turtle.pensize(pensize)
    turtle.forward(distance)
    turtle.left(angle)


if __name__ == "__main__":
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color("DarkGreen")

    view = Screen()
    view.bgcolor("black")

    distance = 30
    max_speed = 10
    max_moves = 100
    max_pen_size = 15
 
    colors = ["DarkMagenta", "DarkSlateBlue", "DodgerBlue4", "green4", "HotPink4", "firebrick4", "gold", "aquamarine"]
    angles = [0, 90, 180, 270]
 
    for _ in range(max_moves):
        color = random.choice(colors)
        angle = random.choice(angles)
        speed = random.randint(1,max_speed)
        pensize = random.randint(1, max_pen_size)
        draw_random(angle, distance, color, turtle, speed, pensize)

    input("Press enter to quit")