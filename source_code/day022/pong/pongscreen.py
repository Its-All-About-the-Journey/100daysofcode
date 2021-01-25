from turtle import Screen

from pong.pongpaddle import PongPaddle

class PongScreen:

    SCR_WIDTH = 800
    SCR_HEIGHT = 600
    SCR_BGCOLOR = "black"
    SCR_TITLE = "PONG"

    def __init__(self) -> None:
        self.screen = Screen()
        self.setup()

    def exitonclick(self) -> None:
        self.screen.exitonclick()

    def onkey(self, key: str, fun: object) -> None:
        self.screen.onkey(key=key, fun=fun)

    def screensize(self):
        return self.screen.screensize()

    def setup(self) -> None:
        self.screen.setup(self.SCR_WIDTH, self.SCR_HEIGHT)
        self.screen.bgcolor(self.SCR_BGCOLOR)
        self.screen.title(self.SCR_TITLE)
        self.screen.tracer(0)
        self.screen.listen()
   
    def update(self) -> None:
        self.screen.update()