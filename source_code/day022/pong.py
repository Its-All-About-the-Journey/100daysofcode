from turtle import Turtle, Screen
import time
from ball import Ball
from paddle import Paddle
from score import Score

GAME_BOARD_WIDTH = 800
GAME_BOARD_HEIGHT = 600

timer = .1
player1 = Paddle(-388)
player2 = Paddle(380)
ball = Ball()
player1_score = Score("player1")
player2_score = Score("player2")

def center_line():
    center_line = Turtle()
    center_line.hideturtle
    center_line.penup()
    center_line.shape("square")
    center_line.shapesize(stretch_len=1, stretch_wid=.25)
    center_line.color("white")
    center_line.goto(0,400)
    center_line.left(270)
    for i in range(1,30):
        center_line.stamp()
        center_line.forward(40)

game_board = Screen()
game_board.setup(width=GAME_BOARD_WIDTH, height=GAME_BOARD_HEIGHT)
game_board.bgcolor("black")
game_board.title("Pong")
game_board.tracer(0)

center_line()

game_board.listen()
game_board.onkeypress(key="w", fun=player1.up)
game_board.onkeypress(key="s", fun=player1.down)
game_board.onkeypress(key="Up", fun=player2.up)
game_board.onkeypress(key="Down", fun=player2.down)

game_over = False
while game_over == False:
    game_board.update()
    time.sleep(ball.timer)
    ball.move()
    if ball.xcor() > -90 and ball.xcor() < 90:
        ball.can_be_hit = True
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()
    if ball.distance(player1) < 30 and ball.xcor() < -320 or ball.distance(player2) < 40 and ball.xcor() > 330:
        ball.hit()
        ball.can_be_hit = False
    if ball.xcor() > 390:
        player1_score.increase_score("player1")
        ball.reset()
    if ball.xcor() < -390:
        player2_score.increase_score("player2")
        ball.reset()

game_board.exitonclick()