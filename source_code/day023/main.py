import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

choice = screen.textinput(f"Difficulty", "Choose your difficulty (easy, medium, hard): ".lower())

screen.listen()
screen.onkey(key="Up", fun=player.up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car(choice)
    cars.move()
    for car in cars.cars:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        cars.increase_speed()
        scoreboard.next_level()
        player.reset()

screen.exitonclick()