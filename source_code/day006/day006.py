def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not is_facing_north() and right_is_clear() :
    turn_left()

while not at_goal():
    if is_facing_north() and not wall_in_front():
        move()
    elif not right_is_clear() and not wall_in_front():
        move()
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
        elif not front_is_clear():
            turn_left()