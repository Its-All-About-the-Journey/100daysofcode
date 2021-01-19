import random
from turtle import Turtle, Screen

def draw_shape(sides: int, distance: int, color: str, turtle: Turtle) -> None:
    turtle.pencolor(color)

    for _ in range(sides):
        turtle.forward(distance)
        turtle.left(360/sides)


if __name__ == "__main__":
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.color("DarkGreen")

    view = Screen()
    view.bgcolor("black")

    distance = 100
    min_sides = 3
    max_sides = 10

    colors = ["DarkMagenta", "DarkSlateBlue", "DodgerBlue4", "green4", "HotPink4", "firebrick4", "gold", "aquamarine"]

    # Draw all shapes in dictionary
    for sides in range(min_sides, max_sides + 1):
        color = random.choice(colors)
        colors.remove(color)
        draw_shape(sides, distance, color, turtle)

    input("Press enter to quit")