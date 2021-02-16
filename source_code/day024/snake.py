from turtle import Turtle
SIZE_AND_SPACE = 20
STARTING_LENGTH = 3
SHAPE = "square"
COLOR = "white"

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.can_turn = True
    
    def create_snake(self):
        for i in range(0,STARTING_LENGTH):
            segment = Turtle()
            segment.shape(SHAPE)
            segment.color(COLOR)
            segment.penup()
            segment.goto(i*-SIZE_AND_SPACE,0)
            self.snake.append(segment)

    def add_segment(self, position):
        self.snake[position].shape(SHAPE)
        self.snake[position].color(COLOR)
        self.snake[position].penup()
        self.snake[position].goto(position*-SIZE_AND_SPACE,0)
        self.snake[position].showturtle()

    def extend(self):
        self.position = (len(self.snake))
        self.snake.append(Turtle(visible=False))
        self.add_segment(self.position)

    def reset(self):
        for seg in self.snake:
            seg.hideturtle()
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
    
    def up(self):
        if self.can_turn and self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
            self.can_turn = False

    def down(self):
        if self.can_turn and self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
            self.can_turn = False

    def left(self):
        if self.can_turn and self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
            self.can_turn = False

    def right(self):
        if self.can_turn and self.snake[0].heading() != 180:
            self.snake[0].setheading(0)
            self.can_turn = False

    def move(self):
        for segment in range(len(self.snake)-1, 0, -1):
            self.snake[segment].goto(self.snake[segment-1].xcor(), self.snake[segment-1].ycor())
        self.snake[0].forward(SIZE_AND_SPACE)
        self.can_turn = True