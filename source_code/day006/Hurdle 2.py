def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while at_goal() == False:
    jump()
  

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
