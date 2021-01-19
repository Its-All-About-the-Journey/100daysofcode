from random import choice
import turtle as t

MATRIX = 10
RADIUS = 10
SEPARATION = 50
COLORS = [
    (2, 2, 46), (81, 95, 235), (42, 172, 247), (38, 93, 171), (34, 35, 135), (213, 18, 183), (212, 42, 220),
    (163, 11, 135), (64, 4, 78), (10, 185, 230), (235, 109, 248), (28, 253, 251), (55, 240, 251), (240, 144, 252),
    (190, 226, 250), (169, 165, 249), (247, 196, 250), (202, 252, 246), (1, 250, 248), (4, 232, 231), (0, 246, 253),
    (250, 251, 239), (2, 81, 119), (45, 230, 232), (56, 50, 208)
]
NUM_COLORS = len(COLORS)

def turn_left():
    tig.left(90)

def turn_right():
    tig.right(90)

def move_forward(distance: int):
    tig.forward(distance)

def draw_spot(color: tuple):
    tig.pendown()
    tig.pencolor(color)
    tig.fillcolor(color)
    tig.begin_fill()
    tig.circle(RADIUS)
    tig.end_fill()
    tig.penup()

def random_color() -> tuple:
    return choice(COLORS)

if __name__ == "__main__":
    tig = t.Turtle()
    tig.shape("turtle")
    tig.color("DarkGreen")
    tig.speed(80)
    t.colormode(255)
    tig.penup()

    view = t.Screen()
    view.bgcolor("black")

    toggle_turn = True

    for i in range(MATRIX):
        draw_spot(random_color())

        for j in range(MATRIX - 1):
            move_forward(SEPARATION)
            draw_spot(random_color())
            
        
        if toggle_turn:
            turn_left() 
            move_forward(SEPARATION)
            turn_left()
        else:
            turn_right()
            move_forward(SEPARATION - RADIUS * 4)
            turn_right()

        toggle_turn = not toggle_turn
    
    input("Press enter to quit")