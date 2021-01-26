# 100 Days of Code : Python
# Pong Game : Main
# Adam Pawlowski (@hypermanganate)

from board import GameBoard
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from time import sleep

GAME_WIDTH = 800
GAME_HEIGHT = 600

# Paddle is 10Lx50H


def player_paddle_up():
    global player_paddle
    player_paddle.move("up")


def player_paddle_down():
    global player_paddle
    player_paddle.move("down")


def check_ball_collide_paddle(ball: Ball, paddle: Paddle):
    if abs(ball.xcor() - paddle.xcor()) < 15:
        # print(f"In X Range: Ball - {abs(ball.xcor())}  Paddle - {abs(paddle.xcor())}")
        # print(f"Y Ranging: Ball - {abs(ball.ycor())} Paddle - {abs(paddle.ycor())}")
        if abs(ball.ycor() - paddle.ycor()) < 40:
            return True

    return False


def check_ball_outside_bounds(ball: Ball, x_max: int):
    if abs(ball.xcor()) >= (x_max):
        return True

    return False


my_board = GameBoard(GAME_WIDTH, GAME_HEIGHT)
computer_paddle = Paddle(my_board.computer_start_x, 0, board_y=my_board.board_y_max, speed=20)
player_paddle = Paddle(my_board.player_start_x, 0, board_y=my_board.board_y_max, speed=25)
my_ball = Ball(board_y=my_board.board_y_max,ball_speed=40)
my_scoreboard = Scoreboard(world_height=GAME_HEIGHT, world_width=GAME_WIDTH)

is_game_playing = True

#my_board.screen.listen()
my_board.screen.onkeypress(key="w", fun=player_paddle_up)
my_board.screen.onkeypress(key="s", fun=player_paddle_down)

while is_game_playing:
    sleep(0.09)
    my_board.screen.update()
    computer_paddle.move_self(my_ball.ycor())
    if check_ball_collide_paddle(my_ball, computer_paddle) or check_ball_collide_paddle(my_ball, player_paddle):
        my_ball.move_ball(collide=True)
    else:
        if check_ball_outside_bounds(my_ball, my_board.board_x_max):
            if my_ball.xcor() > 0:
                # Computer Scored On
                my_scoreboard.add_point_player()
                my_ball.reset()
            else:
                # Player Scored On
                my_scoreboard.add_point_computer()
                my_ball.reset()

            if my_scoreboard.player_score >= 3:
                my_scoreboard.end_game(win=True)
                is_game_playing = False
            if my_scoreboard.computer_score >= 3:
                my_scoreboard.end_game()
                is_game_playing = False

        else:
             my_ball.move_ball(collide=False)

my_board.screen.exitonclick()
