from library import turn_right
from library import move_to_goal
while not wall_in_front():
    move()
turn_left()
while not at_goal():
    move_to_goal()
	
#Library:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_to_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()