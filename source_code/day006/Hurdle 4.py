def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    move()
    while front_is_clear():
        move()
    turn_left()
while at_goal() == False:
    if front_is_clear() == True:
        move()
    elif front_is_clear() == False:
        jump()
  

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
