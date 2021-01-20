
# DAY 18

Python Turtle Hirst Painting

# Description

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

Colorgram

# How to run script
```
Configure the requested parameters such as:
DOT_SIZE - radius of dot
DIMENSION - general overall canvas size
SPACER - extra buffer between rows and dots, multipler to stretch
NUM_COLORS - how large the color palette should be
```

# Sample output
![Sample of Artwork][dotart.png]

# Other Exercises

## Draw a square
```
from turtle import Turtle, Screen

my_turtle = Turtle()

my_turtle.shape("classic")
my_turtle.color("DarkOrange1")

for i in range(0,4):
    my_turtle.forward(100)
    my_turtle.left(90)

my_screen = Screen()
my_screen.exitonclick()
```

## Draw a dashed line
```
from turtle import Turtle, Screen

my_turtle = Turtle()

my_turtle.shape("classic")
my_turtle.color("DarkOrange1")

turtle_pen_status = True # It appears it is down by default

for _ in range(20):
    my_turtle.pen({'pendown': turtle_pen_status})
    my_turtle.forward(10)
    if turtle_pen_status:
        turtle_pen_status = False
    else:
        turtle_pen_status = True

my_screen = Screen()
my_screen.exitonclick()
```

## Multi Shape Doer

```
from turtle import Turtle, Screen
from random import randint

my_turtle = Turtle()

my_turtle.shape("classic")
my_turtle.color("DarkOrange1")

for shape in range(3,11):
    my_turtle.pencolor(f"#{'{:02x}'.format(randint(0,255))}{'{:02x}'.format(randint(0,255))}{'{:02x}'.format(randint(0,255))}")
    for side in range(shape):
        my_turtle.forward(100)
        my_turtle.left(360/shape)

my_screen = Screen()
my_screen.exitonclick()
```

## Turtle Walkabout

```
from turtle import Turtle, Screen
from random import randint

NUMBER_OF_STEPS = 100
STEP_SIZE = 25

my_turtle = Turtle()

my_turtle.shape("classic")
my_turtle.color("DarkOrange1")
my_turtle.pensize(10)

for step in range(0,NUMBER_OF_STEPS + 1):
    my_turtle.pencolor(f"#{'{:02x}'.format(randint(0,255))}{'{:02x}'.format(randint(0,255))}{'{:02x}'.format(randint(0,255))}")
    my_turtle.seth(randint(1,5) * 90)
    my_turtle.forward(STEP_SIZE)

my_screen = Screen()
my_screen.exitonclick()
```

## Tuple/RGB

At this point we moved on to the RGB tuple, and yes, in the documentation the above would be slickely more understandable and I would need the hex format so:
```
my_turtle.colormode(255) # to specify RGB otherwise 1.0 for a single value ???
my_turtle.pencolor(randint(0,255),randint(0,255),randint(0,255))
```

I didn't write any additional code here.

## "A Spirograph" aka Circotwerkulator

```
from turtle import Turtle, Screen, TurtleScreen
from random import randint

RADIUS = 100.0
NUMBER_OF_STEPS = 360
STEP_SIZE = 18

my_turtle = Turtle()

my_turtle.shape("classic")
my_turtle.color("DarkOrange1")
my_turtle.pensize(10)
my_turtle.seth(0)
my_turtle.speed(0)

turns = NUMBER_OF_STEPS // STEP_SIZE

for _ in range(turns):
    my_turtle.pencolor(f"#{'{:02x}'.format(randint(0,255))}{'{:02x}'.format(randint(0,255))}{'{:02x}'.format(randint(0,255))}")
    my_turtle.circle(RADIUS)
    new_heading = my_turtle.heading() + STEP_SIZE
    my_turtle.seth(new_heading)
    
my_screen = Screen()
my_screen.exitonclick()
```