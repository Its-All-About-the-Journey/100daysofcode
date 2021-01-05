def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_forward():
    if not at_goal():
        move()
        
while front_is_clear():
    move_forward()

while not at_goal():
    while front_is_clear() and wall_on_right():
        move_forward()
    if front_is_clear() and right_is_clear():
        turn_right()
        while front_is_clear():
            move_forward()
    elif wall_in_front() and wall_on_right():
        turn_left()
    if wall_in_front() and right_is_clear():
        turn_right()
        if front_is_clear():
            move_forward()