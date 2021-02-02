from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)
screen.colormode(255)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
	screen.update()
	snake.move_segments()

	# Detect collision with food
	if snake.head.distance(food) < 15:
		food.hideturtle()
		food = Food()
		score.increase_score()
		snake.extend()

	# Detect collision with wall
	if abs(snake.head.xcor()) > 299 or abs(snake.head.ycor()) > 299:
		score.reset()
		snake.reset()

	# Detect collision with tail
	for segment in snake.segments[1:]:
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.reset()


screen.exitonclick()