from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title('My Pong Game')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')

game_on = True

while game_on:
	screen.update()
	ball.start_move()

	# Detect collision with top or bottom wall
	if abs(ball.ycor()) >= 290:
		ball.reverse_y()

	# Detect collision with either paddle
	if ball.collision(r_paddle, l_paddle):
		ball.reverse_x()

	if ball.xcor() < -420:
		scoreboard.update_p2_score()
		ball.reset_position()
	elif ball.xcor() > 420:
		scoreboard.update_p1_score()
		ball.reset_position()

	if scoreboard.game_over():
		game_on = False

screen.exitonclick()
