
# DAY 6

# Description

# Environment
OS: OS X

Python version: 3.9.1

# Dependencies

# How to run script
```
enter instructions here
```

# Sample output
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_right()
        while wall_in_front():
            turn_left()
```
