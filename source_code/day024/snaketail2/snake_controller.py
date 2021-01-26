import time

from snaketail2.scoreboard import Scoreboard
from snaketail2.snake_defaults import SnakeDefaults as CFG
from snaketail2.snake_food import SnakeFood
from snaketail2.snake_model import Snake
from snaketail2.snake_view import SnakeView

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
        self.snake.setheading(heading)
    
    def snake_collision(self):
        for segment in self.snake.tail_segments:
            if self.snake.distance(self.snake.tail_segments[segment]) < 10:
                return True
        
        return False

    def wall_collision(self) -> bool:
        position = self.snake.position()

        screen_x = CFG.SCREEN["width"] / 2
        screen_y = CFG.SCREEN["height"] / 2

        top_wall    =   screen_y + CFG.SCREEN["top_wall_offset"]
        bottom_wall = - screen_y + CFG.SCREEN["bottom_wall_offset"]
        right_wall  =   screen_x + CFG.SCREEN["right_wall_offset"]
        left_wall   = - screen_y + CFG.SCREEN["left_wall_offset"]

        return ( 
            position[0] > right_wall or
            position[0] < left_wall or
            position[1] > top_wall or
            position[1] < bottom_wall
        )

    def run(self) -> None:
        game_is_on = True

        # Hack, pause so user can click on game screen.
        time.sleep(1.5)

        while game_is_on:
            self.snake.move()
            self.scoreboard.refresh()
            self.screen.update()     

            if self.collision():
                self.scoreboard.game_over(CFG.SCOREBOARD["gameover_msg"], CFG.SCOREBOARD["gameover_offset"])
                game_is_on = False

            #if self.snake.distance(self.food) < 15: #self.food.shapesize()[0]:
            if self.snake.distance(self.food) < CFG.FOOD["yum_distance"]:
                self.scoreboard.increment()
                self.food.respawn()
                self.snake.extend_tail()

            time.sleep(CFG.TURTLE["speed"])

        # Dump hi score to file
        self.scoreboard.dump_high_score()

        self.screen.exitonclick()
        
        