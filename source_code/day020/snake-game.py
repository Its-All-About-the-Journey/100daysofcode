from turtle import Turtle, Screen, heading
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
GAME_BOARD_SIZE = 600

my_screen = Screen()
my_screen.setup(width=GAME_BOARD_SIZE, height=GAME_BOARD_SIZE)
my_screen.bgcolor("black")
my_screen.title("Thlithery Thnake")
my_screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Right", fun=snake.right)

game_over = False

while not game_over:
    my_screen.update()
    time.sleep(.15)
    snake.move()
    if snake.head.distance(food) <= 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() >= (GAME_BOARD_SIZE/2)+1 or snake.head.xcor() <= -((GAME_BOARD_SIZE/2)+1) or snake.head.ycor() >= (GAME_BOARD_SIZE/2)+1 or snake.head.ycor() <= -((GAME_BOARD_SIZE/2)+1):
        score.game_over()
        game_over = True
    
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_over = True      

my_screen.listen()
my_screen.exitonclick()