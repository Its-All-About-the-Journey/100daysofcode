# 100 Days of Code: Python
# Snake Game: Segment Class
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle

ROY_G_BIV = {
    'red': (209, 0, 0),
    'orange': (255, 102, 34),
    'yellow': (255, 218, 33),
    'green': (51, 221, 0),
    'blue': (17, 51, 204),
    'indigo': (75, 0, 130),
    'violet': (51, 0, 68)
}


class Segment:
    def __init__(self, pos_x: int, pos_y: int, segment_number: int) -> None:
        super().__init__()

        self.segment_number = segment_number
        self.turtle = Turtle("square")
        self.turtle.pu()
        self.turtle.goto(pos_x, pos_y)
        self.turtle_color = \
            list(ROY_G_BIV)[self.segment_number % len(list(ROY_G_BIV))]
        self.turtle.color(ROY_G_BIV[self.turtle_color])

        self.move_queue = []
