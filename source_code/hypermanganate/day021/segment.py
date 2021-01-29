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


class Segment(Turtle):
    def __init__(self, pos_x: int, pos_y: int, segment_number: int) -> None:
        super().__init__()

        self.segment_number = segment_number
        self.shape("square")
        self.pu()
        self.goto(pos_x, pos_y)
        self.turtle_color = \
            list(ROY_G_BIV)[self.segment_number % len(list(ROY_G_BIV))]
        self.color(ROY_G_BIV[self.turtle_color])

    def next_color(self):
        rgb = (int(self.color()[0][0]), int(self.color()[0][1]), int(self.color()[0][2]))
        current_color = list(ROY_G_BIV.values()).index(rgb)
        current_color -= 1
        if current_color < 0:
            current_color = len(list(ROY_G_BIV)) - 1
        self.color(ROY_G_BIV[list(ROY_G_BIV.keys())[current_color]])
