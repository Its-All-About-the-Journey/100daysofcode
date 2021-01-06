
# DAY 6

# Description
Today's video went over while loops and indentation.

All code was using this robot animation site:
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json

# Environment
OS: OS X

Python version: 3.7.6

# Dependencies
None

# How to run script
N/A

# Sample output
section 6.62 - Variable hurdles
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def up_wall():
    turn_left()
    while wall_on_right():
        move()
    
    turn_right()
    down_wall()

def down_wall():
    move()
    turn_right()
    while front_is_clear():
        move()
    
    turn_left()
    
    
while not at_goal():    
    if wall_in_front():
        up_wall()
    else:
        move()
```

section 6.63 - Escaping Maze

Results:
- problem_world: 60
- problem_world2: 34
- problem_world3: 45

```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    # If right is clear, turn R and move
    if right_is_clear() and wall_in_front(): # Always want to move right =)
        turn_right()
        move()
        
    # No wall in front
    elif not wall_in_front():     
        move()
        
    # Turn L
    else:
        turn_left()     
```
