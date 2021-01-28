from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
snake.initialize_snake()
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

screen.exitonclick()



