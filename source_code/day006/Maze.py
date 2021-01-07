def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()
while at_goal() == False:
    if front_is_clear() and wall_on_right():
        move()
    elif right_is_clear() and not front_is_clear():
        turn_right()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
