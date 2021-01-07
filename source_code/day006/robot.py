class Robot():
    def __init__(this):
        this.r = {"n": ("e", "w"), "e": ("s", "n"),
                  "s": ("w", "e"), "w": ("n", "s")}
        while not is_facing_north():
            turn_left()
        this.facing = "n"
    
    def face(this, way):
        if this.facing == way: return this
        turn_left()
        if not this.facing == this.r[way][0]:
            turn_left()
        if this.facing == this.r[way][1]:
            turn_left()
        this.facing = way
        return this
        
    def go(this, way, single = None):
        this.face(way)
        if single:
            move()
        else:
            while not wall_in_front():
                move()
        return this
    
# This is Rob. He wants to reach the flag. Can you help him?
rob = Robot()

# These are the directions he can go: north, east, south, west.
n, e, s, w = "n", "e", "s", "w"

# This pattern will solve 11 of his possible 25 starting positions
rob.go(n).go(e).go(s).go(e)

# This pattern will solve his remaining 14 starting positions
if not at_goal():
    rob.go(w, 1).go(n).go(w).go(n).go(e).go(s).go(e)