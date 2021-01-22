import time

from snaketail.snake_defaults import SnakeDefaults as CFG
from snaketail.snake_model import Snake
from snaketail.snake_view import SnakeView

class SnakeController:
    def __init__(self):
        self.snake = Snake()
        self.screen = SnakeView()
        self.screen.listen()
        self.init_key_bindings()

    def init_key_bindings(self):
        for key in CFG.KEY_BINDINGS:
            function = CFG.KEY_BINDINGS[key]["function"]
            self.screen.screen.onkey(getattr(self, function), key)

    def set_heading_east(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Left"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Right"]["heading"])
        else:
            pass # collision

    def set_heading_north(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Down"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Up"]["heading"])
        else:
            pass # collision

    def set_heading_south(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Up"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Down"]["heading"])
        else:
            pass # collision

    def set_heading_west(self) -> None:
        if not self.snake.heading == CFG.KEY_BINDINGS["Right"]["heading"]:
            self.set_heading(CFG.KEY_BINDINGS["Left"]["heading"])
        else:
            pass # collision

    def set_heading(self, heading: int) -> None:
        self.snake.set_heading(heading)
    
    def run(self) -> None:
        game_is_on = True

        while game_is_on:
            self.screen.update()
            time.sleep(0.3)
            self.snake.move()

        self.screen.exitonclick()