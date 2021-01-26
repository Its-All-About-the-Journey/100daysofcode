from turtle import Turtle

from snaketail2.snake_defaults import SnakeDefaults as CFG

class Snake(Turtle):

    def __init__(self) -> None:

        # Head attributes
        super().__init__(CFG.TURTLE["shape"])
        self.create_head()

        # Tail segment pool for re-using segments
        self.tail_pool = dict()
        self.tail_pool_num = 0
        self.create_tail_pool()

        # The snake's tail segment
        self.tail_segments = dict()
        self.tail_end = -1
        self.tail_head = 0
        self.create_tail()

    
    def create_head(self) -> None:
        # Initialize the snake head
        self.color(CFG.TURTLE["color"])
        self.penup()
        self.goto(0,0)

    def create_tail(self) -> None:
        # Initializes the starting tail
        for position in [(-20,0), (-40,0)]:
            self.add_tail_segment(position)
    
    def create_tail_pool(self) -> None:
        # Creates pre-built segments and stores them in the pool
        for i in range(5):
            segment = self.create_segment( (0,0) )
            segment.hideturtle()

            self.tail_pool_num += 1
            self.tail_pool[self.tail_pool_num] = segment
    
    def tail_pool_pop(self) -> Turtle:
        # Pops a turtle out the tail pool
        # If pool is empty return None
        if self.tail_pool_num == 0:
            return None
        
        segment = self.tail_pool[self.tail_pool_num]
        self.tail_pool_num -= 1

        return segment 
    
    def tail_pool_push(self, segment: Turtle) -> None:
        # Pushing segment into tail pool, let them swim xD
        segment.hideturtle()
        self.tail_pool_num += 1
        self.tail_pool[self.tail_pool_num] = segment
            
    def create_segment(self, position: tuple) -> Turtle:
        # Pop tail segment from tail pool
        new_segment = self.tail_pool_pop()

        # Pool was empty, no more turtles swimming xD
        if not new_segment:
            new_segment = Turtle(CFG.TURTLE["shape"])
        
        new_segment.showturtle()
        new_segment.color(CFG.TURTLE["color"])
        new_segment.penup()
        new_segment.goto(position)

        return new_segment
    
    def add_tail_segment(self, position: tuple) -> None:
        # Adds a segment to the snake tail end
        self.tail_end += 1
        self.tail_segments[self.tail_end] = self.create_segment(position)
    
    def extend_tail(self) -> None:
        # Extends the snake tail 
        self.add_tail_segment( self.tail_segments[self.tail_end].position() )  # TODO: LOOK AT THIS 

    def insert_tail_segment(self, position) -> None:
        # Insert segment as new head
        self.tail_head -= 1
        self.tail_segments[self.tail_head] = self.create_segment(position)
    
    def remove_tail_end(self):
        # Pushes last tail segment into tail pool
        # then deletes from the tail segment
        #self.tail_segments[self.tail_end].hideturtle()

        self.tail_pool_push(self.tail_segments[self.tail_end])

        del self.tail_segments[self.tail_end]
        
        self.tail_end -= 1

    def move(self) -> None:
        # Remove the last tail segment, snake is moving
        self.remove_tail_end()

        # Get the the head's current position and
        # add segment to the tail's head
        self.insert_tail_segment( self.position() )
        
        # Move snake forward by step_len
        self.forward(CFG.TURTLE["step_len"])