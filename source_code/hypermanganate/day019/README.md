
# DAY 19

Turtle Race

# Description

"Race" turtles from left to right to see which one wins.

# Environment

OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

Core only

# How to run script
```
Call the script.

Choose the turtle you think will win from the colors of the rainbow:

Red, Orange, Yellow, Blue, Green, Indigo, and Violet.

Watch and eventually you'll find out which turtle has won!

```

# Sample output
```
You predict the GREEN turtle will win.
Good luck, and let's find out!

And they're off!

ORANGE has taken the lead!
ORANGE is keeping ahead!
VIOLET has taken the lead!
Is VIOLET going to run away with this one?
RED has taken the lead!
VIOLET is out in front!
Is VIOLET going to run away with this one?

...and it's the VIOLET turtle who takes the win!
```

![Sample of Game](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/day019/sample.png


# Other Exercises

## Move Turtle With Key

```
from turtle import Turtle, Screen


def move_forward():
    my_turtle.forward(50)


my_screen = Screen()
my_turtle = Turtle()

my_screen.listen()
my_screen.onkey(key="Up", fun=move_forward)

my_screen.exitonclick() 
 
```

## Etch A Sketch
```
from turtle import Turtle, Screen

STEP_SIZE = 5

class Sketch_A_Etch:

    etcher = Turtle()
    
    def move_forward(self):
        self.etcher.forward(STEP_SIZE)

    def move_backward(self):
        self.etcher.backward(STEP_SIZE)

    def turn_left(self):
        self.etcher.right(10)

    def turn_right(self):
        self.etcher.left(10)

    def clear(self):
        self.etcher.pu()
        self.etcher.home()
        self.etcher.clear()
        self.etcher.pd()


my_screen = Screen()
my_screen.bgcolor("azure3")
etch_a_sketch = Sketch_A_Etch()

my_screen.listen()
my_screen.onkeypress(key="w", fun=etch_a_sketch.move_forward)
my_screen.onkeypress(key="s", fun=etch_a_sketch.move_backward)
my_screen.onkeypress(key="a", fun=etch_a_sketch.turn_left)
my_screen.onkeypress(key="d", fun=etch_a_sketch.turn_right)
my_screen.onkeypress(key="c", fun=etch_a_sketch.clear)

my_screen.exitonclick()
```
