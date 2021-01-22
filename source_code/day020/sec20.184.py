import time

from snaketail.snake_model import Snake
from snaketail.snake_view import SnakeView

if __name__ == "__main__":
    snake = Snake()
    screen = SnakeView()

    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(0.3)
        snake.move()

    screen.exitonclick()