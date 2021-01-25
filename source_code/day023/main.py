import random
import time

from turtle import Screen
from player import Player
from object_manager import ObjectManager
from scoreboard import Scoreboard

FINISH_LINE = 0, 280
START_LINE = 0, -280
SCOREBOARD_POS = -280, 260

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()

    player = Player(START_LINE)

    # Bind key to player move
    screen.onkeyrelease(key="Up", fun=player.move_up)

    obj_manager = ObjectManager()

    scoreboard = Scoreboard(SCOREBOARD_POS)

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        # Did the turtle cross finish line?
        if player.distance(FINISH_LINE) < 20:
            # Reset
            player.reset()

            # Increase object speed
            obj_manager.increase_speed()

            # Increase level and refresh scoreboard
            scoreboard.level_up()
            scoreboard.refresh()

        # Create another object.  1 in 6 chance it will create one
        if random.randint(1, 6) == 1:
            obj_manager.create_object()

        # Move objects
        obj_manager.move()

        # Check for collision with objects
        for obj in obj_manager.all_objects:
            # Collision test
            if obj.distance(player) < obj.shapesize()[0] * 20:
                game_is_on = False

    # Game over
    screen.exitonclick()
