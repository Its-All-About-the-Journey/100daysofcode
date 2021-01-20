from turtlerace import turtle_model as t_model
from turtlerace import turtle_view as tr_view

class TurtleRace:
    
    def __init__(self):
        self.colors = ["blue", "brown", "green", "orange", "red", "yellow"]
        self.num_turtles = 0
        self.view_offset = 10, 30
        self.turtles = dict()
        self.race_view = tr_view.TurtleRaceView("black")
        self.setup_turtles()

    def setup_turtles(self):
        self.num_turtles = len(self.colors)
        y_offset = self.race_view.height / self.num_turtles
        x_pos = self.view_offset[0] - self.race_view.width / 2
        y =  self.race_view.height / 2 - self.view_offset[1]

        for color in self.colors:
    
            home = x_pos, y  
            turtle = t_model.TurtleModel(color, home)
            self.turtles[color] = turtle
            y -= y_offset

    def winner(self) -> object:
        for turtle in self.turtles:
            self.turtles[turtle].forward()

            if self.turtles[turtle].position()[0] >= self.race_view.width / 2:
                return self.turtles[turtle].color

    def rehome(self):
        for turtle in self.turtles:
            self.turtles[turtle].clear()
            self.turtles[turtle].penup()
            self.turtles[turtle].rehome()
            self.turtles[turtle].pendown()
    
    def race(self) -> str:
        self.rehome()
        winner = False

        while not winner:
            winner = self.winner()
        
        return winner

    def run(self):
        
        title = "Turtle power, Cowabunga Dude!"
        prompt = "Choose your color: "

        player_quit = False

        while not player_quit:
            user_choice = self.race_view.text_input(title, prompt)
            
            winning_color = self.race()

            result = "You won!" if winning_color == user_choice else "You lost!"

            new_prompt = (
                f"{result}\n"
                f"Teenage Mutant Turtles always WIN, have a slice of pizza!\n\n"
                f"Do you want to play again? y or n: "
            )

            play_again = user_choice = self.race_view.text_input(title, new_prompt)

            player_quit = not (play_again == 'y')



        
        
        self.race_view.exitonclick()