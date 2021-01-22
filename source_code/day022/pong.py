from time import sleep
from turtle import Turtle, Screen
from random import randint, choice

class PongGame:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.screen.setup(width=900, height=900)
        self.boundaries = {
            "ceiling": self.screen.window_height() // 2 - 60,
            "right_wall": self.screen.window_width() // 2 - 30,
            "floor": self.screen.window_height() // -2 + 60,
            "left_wall": self.screen.window_width() // -2 + 30
        }
        
        self.draw_center_line()
        
        self.player1 = Paddle("left", self.boundaries)
        self.player2 = Paddle("right", self.boundaries)
        
        self.ball = Ball(self.boundaries, (self.player1, self.player2))
        
        self.scoreboard = Scoreboard()
        
        # t1.goto(-380, 69)
        # t2.goto(-380, -69)
        # t3.goto(380, 69)
        # t4.goto(380, -69)
        
        self.screen.onkeypress(self.player1.move_up, "w")
        self.screen.onkeypress(self.player1.move_down, "s")
        self.screen.onkeypress(self.player2.move_up, "Up")
        self.screen.onkeypress(self.player2.move_down, "Down")
        self.screen.onkeyrelease(self.player1.stop, "w")
        self.screen.onkeyrelease(self.player1.stop, "s")
        self.screen.onkeyrelease(self.player2.stop, "Up")
        self.screen.onkeyrelease(self.player2.stop, "Down")
        self.screen.listen()

        self.run()
        self.screen.mainloop()
        
    def draw_center_line(self):
        self.screen.tracer(0)
        artists = [Turtle() for _ in range(18)]
        spot = 440
        spacing = 50
        for artist in artists:
            artist.hideturtle()
            artist.penup()
            artist.pensize(5)
            artist.setheading(270)
            artist.sety(spot)
            artist.pendown()
            spot -= spacing
    
        self.screen.tracer(1)
        for artist in artists:
            artist.forward(25)

    def run(self):
        self.ball.tick()
        self.player1.tick()
        self.player2.tick()

        # ball wall bounce detection
        if (self.ball.ycor() >= self.boundaries["ceiling"] or
                self.ball.ycor() <= self.boundaries["floor"]):
            self.ball.y_direction *= -1
        elif (self.ball.xcor() <= self.boundaries["left_wall"] or
              self.ball.xcor() >= self.boundaries["right_wall"]):
            self.ball.x_direction *= -1

        # ball player bounce detection
        if self.ball.xcor() < 0:
            player_x, player_y = self.player1.position()
            if self.ball.xcor() <= player_x:
                if self.ball.ycor() <= player_y + 69 and self.ball.ycor() >= player_y - 69:
                    self.ball.x_direction *= -1
        else:
            player_x, player_y = self.player2.position()
            if self.ball.xcor() >= player_x:
                if self.ball.ycor() <= player_y + 69 and self.ball.ycor() >= player_y - 69:
                    self.ball.x_direction *= -1

        # ball kill detection
        if self.ball.xcor() <= self.boundaries["left_wall"]:
            self.is_moving = False
            self.scoreboard.player2()
            self.ball.start_over()
        if self.ball.xcor() >= self.boundaries["right_wall"]:
            self.is_moving = False
            self.scoreboard.player1()
            self.ball.start_over()
            
        if self.scoreboard.player1score >= 3 or self.scoreboard.player2score >= 3:
            self.scoreboard.game_over()
            self.running = False
        
        if self.running:
            self.screen.ontimer(self.run, 1)

class Paddle(Turtle):
    def __init__(self, side, boundaries):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=6) # 60 + 60 = 120
        self.setheading(90)
        self.is_moving = False
        self.direction = None
        if side == "left":
            self.setx(-400)
        else:
            self.setx(400)
        self.ceiling = boundaries["ceiling"]
        self.floor = boundaries["floor"]
            
    def tick(self):
        if self.is_moving:
            if self.direction == self.forward and self.ycor() < self.ceiling:
                self.direction(25)
            if self.direction == self.backward and self.ycor() > self.floor:
                self.direction(25)
            
    def move_up(self):
        self.is_moving = True
        self.direction = self.forward
    
    def move_down(self):
        self.is_moving = True
        self.direction = self.backward
        
    def stop(self):
        self.is_moving = False
        
    def scored(self):
        pass
        
class Ball(Turtle):
    def __init__(self, boundaries, players):
        super().__init__()
        self.shape("square")
        self.penup()
        self.is_moving = True
        self.x_speed = 5
        self.y_speed = 5
        self.x_direction = choice([1, -1])
        self.y_direction = choice([1, -1])
        self.boundaries = boundaries
        self.sety(randint(self.boundaries["floor"], self.boundaries["ceiling"]))
        self.players = players
        
    def tick(self):
        if self.is_moving:
            x = self.xcor() + (self.x_speed * self.x_direction)
            y = self.ycor() + (self.y_speed * self.y_direction)
            self.goto(x, y)
            
    def start_over(self):
        self.x_direction = choice([1, -1])
        self.y_direction = choice([1, -1])
        self.setx(0)
        self.sety(randint(self.boundaries["floor"], self.boundaries["ceiling"]))
        sleep(3)
        self.is_moving = True

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 360)
        self.player1score = 0
        self.player2score = 0
        self.update()
    
    def player1(self):
        self.player1score += 1
        self.update()
    
    def player2(self):
        self.player2score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"{self.player1score}   {self.player2score}", False, align="center", font=("Agency FB", 48, "bold"))
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, align="center", font=("Agency FB", 48, "bold"))
        
game = PongGame()