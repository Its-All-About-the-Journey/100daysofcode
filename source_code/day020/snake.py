from time import sleep
from turtle import Turtle, Screen
import math

class Snake:
    
    
    def __init__(self):
        """a new snake is born"""
        
        # move directions
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        
        # body segments
        self.SEGWIDTH = 21
        self.segments = []
    
        # create the head and two additional segments
        for i in range(30):
            segment = Turtle(shape="square")
            segment.penup()
            segment.setx(i * self.SEGWIDTH * -1)  # shift left to make a snake
            self.segments.append(segment)
    
        self.head = self.segments[0]
        self.update_color()
        return None
    
        
    def slither(self):
        """the snake slithers on"""
        
        # move all segments, from tail to neck, into the segment's position ahead of it
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
    
        # now move the head
        self.head.forward(self.SEGWIDTH)
        return self
    
    
    def update_color(self):
        for i in range(len(self.segments)):
            self.segments[i].color(
                int((math.sin((.3 * i) + 0) * 127) + 127.5),
                int((math.sin((.3 * i) + 2) * 127) + 127.5),
                int((math.sin((.3 * i) + 4) * 127) + 127.5)
            )
    
        
    def face_up(self):
        if self.head.heading() not in [self.UP, self.DOWN]:
            self.head.setheading(self.UP)
        return self
    
    
    def face_down(self):
        if self.head.heading() not in [self.DOWN, self.UP]:
            self.head.setheading(self.DOWN)
        return self
    
    
    def face_left(self):
        if self.head.heading() not in [self.LEFT, self.RIGHT]:
            self.head.setheading(self.LEFT)
        return self
    
    
    def face_right(self):
        if self.head.heading() not in [self.RIGHT, self.LEFT]:
            self.head.setheading(self.RIGHT)
        return self
    
    
screen = Screen()
screen.setup(width = 600, height = 600)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.onkey(snake.face_up, "Up")
screen.onkey(snake.face_down, "Down")
screen.onkey(snake.face_left, "Left")
screen.onkey(snake.face_right, "Right")
screen.listen()

running = True
while running:
    screen.update()
    snake.slither()
    sleep(0.1)
    
screen.exitonclick()