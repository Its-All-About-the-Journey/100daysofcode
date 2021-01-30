#!/usr/bin/env python3
# 100 Day of Code: Python
# Not Frogger: Main Game
# Adam Pawlowski (@hypermanganate)

import time
from turtle import Screen
from player import Player
from car_manager import CarManager, setup_car_shapes
from scoreboard import Scoreboard

SCORE_POS_X = -280
SCORE_POS_Y = 250
NUMBER_OF_CARS = 6

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Simulator 2021")

player = Player()
scoreboard = Scoreboard(pos_x=SCORE_POS_X, pos_y=SCORE_POS_Y)

screen.listen()
screen.onkeypress(fun=player.move_up, key="w")
screen.onkeypress(fun=player.move_down, key="s")

setup_car_shapes(screen)

manager = CarManager(num_cars=NUMBER_OF_CARS, car_speed=scoreboard.score,
                     field_y_min=-250, field_y_max=250)


def next_level(player):
    scoreboard.add_score()
    manager.set_level(scoreboard.score)
    player.reset()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.move_cars()
    if manager.check_for_accidents(player.position()):
        game_is_on = False
        scoreboard.end_game()
    if player.has_reached_goal():
        next_level(player)

screen.exitonclick()
