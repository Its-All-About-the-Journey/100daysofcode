from turtle import Turtle

class PongScoreboard(Turtle):

    def __init__(self, left_pos: tuple, right_pos: tuple, color: str = "white") -> None:
        super().__init__()
        self.score_left = 0
        self.score_left_pos = left_pos
        self.score_right = 0
        self.score_right_pos = right_pos
        self.color(color)
        self.setup()

    def add_point_left(self, points: int = 1) -> None:
        self.score_left += points
        self.refresh()

    def add_point_right(self, points: int = 1) -> None:
        self.score_right += points
        self.refresh()
    
    def refresh(self) -> None:
        self.clear()
        
        self.setposition(self.score_left_pos)
        self.write(f"{self.score_left}", font=("Verdana", 15, "normal"))

        self.setposition(self.score_right_pos)
        self.write(f"{self.score_right}", font=("Verdana", 15, "normal"))
    
    def setup(self) -> None:
        self.hideturtle()
        self.penup()
        self.refresh()