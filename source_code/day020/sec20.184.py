import time

from snaketail.snake_model import Snake
from snaketail.snake_view import SnakeView

def init_screen():
    self.screen.setup(width=600, height=600)
    self.screen.bgcolor("black")
    self.screen.title("The Python Game")
    self.screen.tracer(0)

if __name__ == "__main__":
    snake = Snake()
    screen = SnakeView()

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.3)
        snake.move()

    screen.exitonclick()