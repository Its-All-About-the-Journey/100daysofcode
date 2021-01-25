import time

from pong.pongball import PongBall
from pong.pongpaddle import PongPaddle
from pong.pongscoreboard import PongScoreboard
from pong.pongscreen import PongScreen

class PongGame:

    R_PDL_POSITION = (350,0)
    L_PDL_POSITION = (-350, 0)
    R_SCORE_POS = 100, 250
    L_SCORE_POS = -100, 250
    BALL_PAD_MAX_DIST = 50
    
    def __init__(self) -> None:
        self.screen = PongScreen()
        self.ball = PongBall()
        self.r_paddle = PongPaddle(self.R_PDL_POSITION)
        self.l_paddle = PongPaddle(self.L_PDL_POSITION)
        self.scoreboard =  PongScoreboard(self.L_SCORE_POS, self.R_SCORE_POS)
        self.setup_key_bindings()

    def ball_paddle_collision(self, paddle: PongPaddle) -> None:
        x_collision = abs(self.ball.xcor()) > abs(paddle.position()[0]) - 20
        y_collision = self.ball.distance(paddle) < self.BALL_PAD_MAX_DIST

        if  x_collision and y_collision:
            self.ball.bounce_x()

    def ball_missed(self) -> None:
        ball_x_pos = self.ball.xcor()

        if ball_x_pos > self.r_paddle.xcor() or ball_x_pos < self.l_paddle.xcor():
            self.ball.reset_position()
            self.scoreboard.add_point_left()

    def ball_wall_collision(self) -> None:
        if abs(self.ball.ycor()) > self.screen.screensize()[1] - 20:
            self.ball.bounce_y()

    def setup_key_bindings(self) -> None:
        # r_paddle
        self.screen.onkey(key="Down", fun=self.r_paddle.move_down)
        self.screen.onkey(key="Up", fun=self.r_paddle.move_up)

        #l_paddle
        self.screen.onkey(key="s", fun=self.l_paddle.move_down)
        self.screen.onkey(key="w", fun=self.l_paddle.move_up)

    def run(self) -> None:
        gameon = True

        # Hack, let player get ready
        time.sleep(1)

        while gameon:
            self.screen.update()
            self.ball.move()

            # Check wall collision
            self.ball_wall_collision()

            # Check paddle collision
            self.ball_paddle_collision(self.r_paddle)
            self.ball_paddle_collision(self.l_paddle)

            # Check if paddle missed ball
            self.ball_missed()
            
            time.sleep(self.ball.move_speed)
        
        self.screen.exitonclick()