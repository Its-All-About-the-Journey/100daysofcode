# DAY 6

Escaping the Maze

# Description

# Environment
OS: Ubuntu Bionic

Python version: 3.6.9

# Dependencies

None

# How to run script
```
```

# Sample output
```
```
# Other Solutions

## Turn robot right
```
def turn_right():
  for iter in range(3): turn_left()
```

## Hurdles
```
def turn_right():
  for iter in range(3): turn_left()

def move_left():
    turn_left()
    move()
    
def move_right():
    turn_right()
    move()
    
def jump(times):
    for iter in range(times):
        move_left()
        move_right()
        move_right()
        turn_left()
         
# Main
for iter in range(0, 6):
  move()
  jump(1)
```

## While Loop Hurdles
```
def turn_right():
  for iter in range(0, 3): turn_left()

def move_left():
    turn_left()
    move()
    
def move_right():
    turn_right()
    move()
    
def jump(times):
    while(times):
        move_left()
        move_right()
        move_right()
        turn_left()
        times -= 1
         
# Main
while not(at_goal()):
  move()
  jump(1)
```

## Random Hurdles
```
def turn_right():
  for iter in range(0, 3): turn_left()

def move_left():
    turn_left()
    move()
    
def move_right():
    turn_right()
    move()
    
def jump(times):
    while(times):
        move_left()
        move_right()
        move_right()
        turn_left()
        times -= 1
         
# Main
while not(at_goal()):
    if wall_in_front():
        jump(1)
    else:
      move()
```

## Random Hurdle Wall Jumper-Overer
```
def turn_right():
  for iter in range(0, 3): turn_left()

def move_left():
    turn_left()
    move()
    
def move_right():
    turn_right()
    move()
    
def jump(times):
    while(times):
        hurdle_height = 0
        move_left()
        while(wall_on_right()):
            move()
            hurdle_height += 1
        move_right()
        move_right()
        while(hurdle_height):
            move()
            hurdle_height -= 1
        turn_left()
        times -= 1
         
# Main
while not(at_goal()):
    if wall_in_front():
        jump(1)
    else:
      move()
```
