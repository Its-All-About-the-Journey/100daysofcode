def turn_right():
    turn_left()
    turn_left()
    turn_left()
rturns = 0
while not at_goal():
    if conrturns == 4:
        turn_left()
        rturns = 0
    else:
        if right_is_clear():
            turn_right()
            move()
            rturns += 1
        elif front_is_clear():
            move()
            rturns -= 1
        else:
            turn_left()
            rturns -= 1