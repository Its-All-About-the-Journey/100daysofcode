from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
screen.bgcolor("beige")

turtle = Turtle()
turtle.shape("turtle")


def square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
        

# square(100)


def dashes(length):
    is_pen_down = True
    for i in range(length + 1):
        if i % 10 == 0:
            is_pen_down = not is_pen_down
        if is_pen_down:
            turtle.down()
        else:
            turtle.up()
        turtle.forward(1)


# dashes(200)


from random import randint, choice


def complex_shape(max_sides):
    shapes = range(3, max_sides + 1)
    for shape in shapes:
        sides = shape
        angle = 360 / sides
        rand_color()
        for side in range(sides):
            turtle.forward(50)
            turtle.right(angle)
            

# complex_shape(11)


import colorgram
colors = colorgram.extract("day18image.png", 32)


def rand_color_img():
    return choice(colors).rgb


def rand_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    turtle.pencolor(r, g, b)

    
turtle.speed(0)


def rand_turn():
    choices = [0, 90, 180, 270]
    turtle.right(choice(choices))


def rand_walk():
    turtle.pensize(10)
    for _ in range(1_000):
        rand_color()
        rand_turn()
        turtle.forward(30)
    

# rand_walk()


def spiro_graph(num_circles):
    for _ in range(num_circles):
        rand_color()
        turtle.setheading(turtle.heading() + (360 / num_circles))
        turtle.circle(100)


# spiro_graph(50)


def dot_grid(rows = 16, cols = 16, dot_size = 25, grid_size = 400):
    turtle.penup()
    
    turtle.setx(grid_size // 2 * -1)
    turtle.sety(grid_size // 2 * -1)
    
    # dot positions per column
    for row in range(rows):
        for col in range(cols):
            turtle.setx(turtle.position()[0] + (grid_size // cols))
            turtle.dot(dot_size, rand_color_img())
        turtle.sety(turtle.position()[1] + (grid_size // rows))
        turtle.setx(grid_size // 2 * -1)
        

dot_grid(10, 10, 20, 400)


screen.exitonclick()