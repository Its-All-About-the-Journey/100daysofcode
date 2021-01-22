from turtle import Turtle

from snaketail.snake_defaults import SnakeDefaults as CFG

class Snake:

    def __init__(self):
        self.segments = list()
        self.init_segments()
        self.head = 0
        self.heading = 0
    
    def init_segments(self) -> None:
        for position in [(0,0), (-20,0), (-40,0)]:
            new_segment = Turtle(CFG.TURTLE["shape"])
            new_segment.color(CFG.TURTLE["color"])
            new_segment.penup()
            new_segment.goto(position)
            self.heading = new_segment.heading()
            self.segments.append(new_segment)

    def set_heading(self, heading: int) -> None:
        self.heading = heading
        self.segments[self.head].setheading(heading)

    def move(self) -> None:
        for seg_num in range(len(self.segments) -1, 0, -1):  # 3 segment code
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.segments[self.head].forward(CFG.TURTLE["step_len"])