from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
    
    def reset(self) -> None:
        self.score = 0
    
    def increment(self, points: int = 1) -> None:
        self.score += points
        self.clear() # Clear scoreboard text
    
    def refresh(self) -> None:
        self.write(f"Score: {self.score}",font=("Verdana", 15, "normal"))
    
    def game_over(self, msg: str, offset: int) -> None:
        self.setposition(0 - offset,0)
        self.write(msg, align="center", font=("Verdana", 24, "bold"))
        