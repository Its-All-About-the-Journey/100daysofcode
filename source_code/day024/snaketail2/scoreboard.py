from turtle import Turtle

class Scoreboard(Turtle):

    HIGH_SCORE_FILENAME = "./snaketail2/highscore.txt"

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        
        self.high_score_loaded = 0
        self.load_high_score()

        self.high_score = self.high_score_loaded
        self.hideturtle()
        self.penup()
        

    def game_over(self, msg: str, offset: int) -> None:
        self.setposition(0 - offset,0)
        self.write(msg, align="center", font=("Verdana", 24, "bold"))

    def increment(self, points: int = 1) -> None:
        self.score += points

        # New hi_score?
        if self.high_score < self.score:
            self.high_score = self.score 

        self.clear() # Clear scoreboard text

    def reset(self) -> None:
        self.score = 0
    
    def load_high_score(self) -> None:
        try:
            with open(self.HIGH_SCORE_FILENAME) as file_in:
                self.high_score_loaded = int(file_in.read())
        except:
            self.high_score_loaded = 0
            print("Could not load file.")

    def refresh(self) -> None:
        self.write(f"Score: {self.score} : Hi-Score: {self.high_score}",font=("Verdana", 15, "normal"))
    
    def dump_high_score(self) -> None:
        if self.high_score > self.high_score_loaded:
            try:            
                with open(self.HIGH_SCORE_FILENAME, "w") as file_out:
                    file_out.write(str(self.high_score))
            except:
                print("Could not write file")
        