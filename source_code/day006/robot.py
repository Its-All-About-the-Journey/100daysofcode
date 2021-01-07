# taking a step forward if we can
def take_a_step():
    if front_is_clear():
        move()

# walking around a right hand corner or wall
def right_turn():
    right_face()
    take_a_step()
    
# walking around a left hand corner or wall
def left_turn():
    left_face()
    take_a_step()
    
# facing right == rotating left 3x
def right_face():
    turn_left()
    turn_left()
    turn_left()
    
# facing left == rotating left
def left_face():
    turn_left()
    
# normalize orientation to the north
while not is_facing_north():
    turn_left()
    
# take initial step forward if possible
take_a_step()

# escape the maze
while not at_goal():
    if not wall_on_right():
        right_turn()
    elif front_is_clear():
        move()
    else:
        left_turn()