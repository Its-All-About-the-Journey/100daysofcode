import time

from snaketail.scoreboard import Scoreboard
from snaketail.snake_defaults import SnakeDefaults as CFG
from snaketail.snake_food import SnakeFood
from snaketail.snake_model import Snake
from snaketail.snake_view import SnakeView

class SnakeController:
    def __init__(self) -> None:
        self.snake = Snake()
        self.screen = SnakeView()
        self.screen.listen()
        self.init_key_bindings()
        self.food = SnakeFood()
        self.scoreboard = Scoreboard()
        self.init_scoreboard()

    def init_key_bindings(self) -> None:
        for key in CFG.KEY_BINDINGS:
            function = CFG.KEY_BINDINGS[key]["function"]
            self.screen.screen.onkeyrelease(getattr(self, function), key)

    def init_scoreboard(self) -> None:
        self.scoreboard.color(CFG.SCOREBOARD["color"])
        self.scoreboard.setposition(
            - CFG.SCOREBOARD["offset_x"],
            CFG.SCREEN["height"] / 2 - CFG.SCOREBOARD["offset_y"]
        )

    def collision(self) -> bool:
        return self.wall_collision() or self.snake_collision()

    def set_heading_east(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Left"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Right"]["heading"])

    def set_heading_north(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Down"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Up"]["heading"])

    def set_heading_south(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Up"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Down"]["heading"])

    def set_heading_west(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Right"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Left"]["heading"])

    def set_heading(self, heading: int) -> None:
        self.snake.set_heading(heading)
    
    def snake_collision(self):
        for segment in self.snake.segments[1::]:
            if self.snake.head_distance(segment) < 10:
                return True
        
        return False

    def wall_collision(self) -> bool:
        position = self.snake.position()
        wall_x = CFG.SCREEN["width"] / 2 - CFG.SCREEN["wall_offset"]
        wall_y = CFG.SCREEN["height"] / 2 - CFG.SCREEN["wall_offset"]

        return ( 
            position[0] > wall_x or
            position[0] < - wall_x or
            position[1] > wall_y or
            position[1] < - wall_y
        )

    def run(self) -> None:
        game_is_on = True

        while game_is_on:
            start = time.time()
            self.scoreboard.refresh()
            self.screen.update()
            self.snake.move()

            if self.collision():
                self.scoreboard.game_over(CFG.SCOREBOARD["gameover_msg"], CFG.SCOREBOARD["gameover_offset"])
                game_is_on = False

            if self.snake.head_distance(self.food) < 15: #self.food.shapesize()[0]:
                self.scoreboard.increment()
                self.food.respawn()
                self.snake.extend_snake()

            lapse = (time.time() - start) * 1000
            
            print(f"Time lapse: {lapse:0.4f} msec")
            
            time.sleep(CFG.TURTLE["speed"])

        self.screen.exitonclick()