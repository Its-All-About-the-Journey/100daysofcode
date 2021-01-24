# 100 Days of Code : Python
# Day 20: Snake Game Foundations
# Adam Pawlowski (@hypermanganate)

from turtle import Screen
from snake import Snake
import time

GAME_HEIGHT = 600
GAME_WIDTH = 600
GAME_TITLE = "Move Snake"


def setup_screen():
    my_screen = Screen()
    my_screen.setup(width=GAME_WIDTH, height=GAME_HEIGHT)
    my_screen.colormode(255)
    my_screen.bgcolor((0, 0, 0))
    my_screen.title(GAME_TITLE)
    my_screen.tracer(0)
    return my_screen


def setup_snake(snake: Snake):
    pos_x = snake.SNAKE_START_X
    pos_y = snake.SNAKE_START_Y

    snake.grow(pos_x=pos_x, pos_y=pos_y, color=(255, 127, 80))
    snake.set_head()
    pos_x -= snake.SNAKE_SEGMENT_WIDTH

    for segment in range(snake.SNAKE_START_SEGMENTS):
        snake.grow(pos_x, pos_y)
        pos_x -= snake.SNAKE_SEGMENT_WIDTH

# This is unnecessary and can be wrapped in the snake.
# This is also where I ghad programmed this, and then in the video
# she builds it with the snake moving "forward" with a changing heading


def move_snake_up():
    if my_snake.direction != my_snake.DIR_DOWN:
        my_snake.direction = my_snake.DIR_UP


def move_snake_left():
    if my_snake.direction != my_snake.DIR_RIGHT:
        my_snake.direction = my_snake.DIR_LEFT


def move_snake_right():
    if my_snake.direction != my_snake.DIR_LEFT:
        my_snake.direction = my_snake.DIR_RIGHT


def move_snake_down():
    if my_snake.direction != my_snake.DIR_UP:
        my_snake.direction = my_snake.DIR_DOWN

# Main


if __name__ == '__main__':

    my_screen = setup_screen()
    my_snake = Snake(GAME_WIDTH, GAME_HEIGHT)
    setup_snake(my_snake)
    my_screen.update()

    my_screen.listen()
    my_screen.onkeypress(key="w", fun=move_snake_up)
    my_screen.onkeypress(key="a", fun=move_snake_left)
    my_screen.onkeypress(key="s", fun=move_snake_down)
    my_screen.onkeypress(key="d", fun=move_snake_right)

    while my_snake.alive:
        my_screen.update()
        time.sleep(0.1)
        my_snake.move_snake()

    print("Snake is no longer alive")

    my_screen.exitonclick()
