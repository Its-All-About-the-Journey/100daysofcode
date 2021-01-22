from turtle import Turtle

from snaketail.snake_defaults import SnakeDefaults as CFG

class Snake:

    def __init__(self):
        self.segments = list()
        self.init_segments()
    
    def init_segments(self):
        for position in [(0,0), (-20,0), (-40,0)]:
            new_segment = Turtle(CFG.TURTLE["shape"])
            new_segment.color(CFG.TURTLE["color"])
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.segments[0].forward(CFG.TURTLE["step_len"])