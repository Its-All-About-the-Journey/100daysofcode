from turtle import Turtle

from snaketail.snake_defaults import SnakeDefaults as CFG

class Snake:

    def __init__(self) -> None:
        self.segments = list()
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self) -> None:
        for position in [(0,0), (-20,0), (-40,0)]:
            self.add_snake_segment(position)
    
    def add_snake_segment(self, position: tuple) -> None:
        new_segment = Turtle(CFG.TURTLE["shape"])
        new_segment.color(CFG.TURTLE["color"])
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend_snake(self) -> None:
        self.add_snake_segment(self.segments[-1].position())

    def is_head(self, turtle: Turtle) -> bool:
        return self.head == turtle

    def head_distance(self, turtle: Turtle) -> int:
        return self.head.distance(turtle)
    
    def heading(self) -> float:
        return self.head.heading()
        
    def position(self):
        return self.head.position()

    def set_heading(self, heading: int) -> None:
        self.head.setheading(heading)

    def move(self) -> None:
        for seg_num in range(len(self.segments) -1, 0, -1):  # 3 segment code
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(CFG.TURTLE["step_len"])