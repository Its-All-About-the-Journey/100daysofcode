from turtle import Turtle
SIZE_AND_SPACE = 20
STARTING_LENGTH = 3
SHAPE = "square"
COLOR = "white"

class Snake:
    def __init__(self):
        self.snake = []
        for i in range(0,STARTING_LENGTH):
            self.snake.append(Turtle())
            self.snake[i].shape(SHAPE)
            self.snake[i].color(COLOR)
            self.snake[i].penup()
            self.snake[i].goto(i*-SIZE_AND_SPACE,0)
        self.head = self.snake[0]
        self.segments = self.snake
        self.can_turn = True

    def add_segment(self, position):
        self.snake.append(Turtle())
        self.snake[position].shape(SHAPE)
        self.snake[position].color(COLOR)
        self.snake[position].penup()
        self.snake[position].goto(position*-SIZE_AND_SPACE,0)
        self.snake[position].showturtle()

    def extend(self):
        self.position = (len(self.snake))
        self.add_segment(self.position)
    
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