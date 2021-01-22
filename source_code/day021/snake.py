from random import randint
from math import hypot, sin
from turtle import Turtle, Screen

class SnakeGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.title("Snake")
        self.screen.bgcolor("black")
        self.screen.colormode(255)
        self.screen.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = Scoreboard()
        self.setup_keybindings()
        self.running = True
        self.run()
        self.screen.mainloop()
    
    def setup_keybindings(self):
        self.screen.onkeyrelease(self.snake.face_up, "Up")
        self.screen.onkeyrelease(self.snake.face_down, "Down")
        self.screen.onkeyrelease(self.snake.face_left, "Left")
        self.screen.onkeyrelease(self.snake.face_right, "Right")
        self.screen.onkeyrelease(self.screen.bye, "Escape")
        self.screen.listen()
    
    def run(self):
        if self.running:
            self.snake.slither()
            self.screen.update()
            if self.snake.has_crashed():
                self.game_over()
            if self.snake.is_eating(self.food):
                self.level_up()
            self.screen.ontimer(self.run, 100)
    
    def level_up(self):
        self.scoreboard.add_point()
        self.snake.add_segment()
        self.food.relocate()
    
    def game_over(self):
        self.running = False
        self.scoreboard.game_over()

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.UP = 90
        self.DOWN = 270
        self.LEFT = 180
        self.RIGHT = 0
        self.SEGWIDTH = 21
        self.segments = []
        self.create_head()
        self.add_segment()
        self.add_segment()
    
    def create_head(self):
        self.head = self.base_segment()
        self.segments.append(self.head)
        self.update_color()
    
    def base_segment(self):
        segment = Turtle(shape="square")
        segment.penup()
        return segment
    
    def add_segment(self):
        segment = self.base_segment()
        segment.goto(self.segments[-1].position())
        self.segments.append(segment)
        self.update_color()
    
    def slither(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(self.SEGWIDTH)
        self.can_turn = True
        return self
    
    def update_color(self):
        self.segments[-1].color(
            int((sin((.3 * len(self.segments)) + 0) * 127) + 127.5),
            int((sin((.3 * len(self.segments)) + 2) * 127) + 127.5),
            int((sin((.3 * len(self.segments)) + 4) * 127) + 127.5)
        )
    
    def face_up(self):
        if self.can_turn and self.head.heading() not in [self.UP, self.DOWN]:
            self.can_turn = False
            self.head.setheading(self.UP)
    
    def face_down(self):
        if self.can_turn and self.head.heading() not in [self.DOWN, self.UP]:
            self.can_turn = False
            self.head.setheading(self.DOWN)
    
    def face_left(self):
        if self.can_turn and self.head.heading() not in [self.LEFT, self.RIGHT]:
            self.can_turn = False
            self.head.setheading(self.LEFT)
    
    def face_right(self):
        if self.can_turn and self.head.heading() not in [self.RIGHT, self.LEFT]:
            self.can_turn = False
            self.head.setheading(self.RIGHT)
    
    def is_eating(self, food):
        return self.head.distance(food) < 7
    
    def has_crashed(self):
        return self.has_collided_with_wall() or self.has_collided_with_wall()
    
    def has_collided_with_wall(self):
        return (self.head.ycor() >= 273
                or self.head.ycor() <= -273
                or self.head.xcor() >= 273
                or self.head.xcor() <= -273)
    
    def has_collided_with_tail(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 7:
                return True
        return False

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("coral")
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.relocate()
    
    def relocate(self):
        while True:
            x, y = randint(-12, 12) * 21, randint(-12, 12) * 21
            dist = hypot(self.position()[0] - x, self.position()[1] - y)
            if dist > 21 * 6:
                self.curr_pos = self.position()
                break
        self.goto(x, y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.reset_board()
    
    def reset_board(self):
        self.score = 0
        self.goto(0, 285)
        self.update_board()
    
    def add_point(self):
        self.score += 1
        self.update_board()
    
    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center")
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center")


game = SnakeGame()