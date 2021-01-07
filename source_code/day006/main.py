#!/usr/bin/env python3
# 100 Days of Code : Day 6 Project
# Reeborg Maze Solver
# Adam Pawlowski (@hypermanganate)

grid_size = 6

grid = []
grid_y = []
directions = [0, 1, 2, 3] # North, East, South, West

# None of the below does anything since I eventually realized you don't have a starting point, and I ran out of time.
# The idea was to "scan" the block were you are, so you could:
#   Breadcrumb and return directly to the last unexplored area when blocked
#   Ascertain if you found the goal by having an unblocked wall outside of the 5x5 playing area
#   Print a representation of the maze
#   I think at least the breadcrumbing and printing is possible, I just don't have time.

def setup_grid():
  for index_x in range(grid_size):
    grid[index_x] = []
    for index_y in range(grid_size):
       grid[index_x][index_y] = directions

def scan(pos_x, pos_y, orientation):
  for iter in range(3):
    orientation = face(iter, orientation)
    if check_orientation:
      grid[pos_x][pos_y].remove(orientation)

  return orientation

def check_orientation():
  if front_is_clear(): return True

  return False

def set_orientation():

  while not (is_facing_north()):
    turn_left()

  return 0


def face(direction, orientation):

  while not (orientation == direction):
    turn_left()
    if orientation == 0:
      orientation = 3
    else: 
      orientation -= 1

  return orientation

def turn_right():

  for iter in range(3): turn_left()

# Main

orientation = set_orientation()

while not (at_goal()):

    print(f"Wall on right: {wall_on_right()}")

    print(f"Front is clear: {front_is_clear()}")

    if front_is_clear() and wall_on_right():

        move()

    elif not wall_on_right():

        turn_right()

        move()

    else:

        turn_left()

