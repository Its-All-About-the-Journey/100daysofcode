# 100 Days of Code: Python
# Pong Game : Game Board
# Adam Pawlowski (@hypermanganate)

from turtle import Screen # not going to use TurtleScreen here at this point, too annoying

GAME_TITLE = "Digital Ping Pong Game"
BLOCK_SIZE = 20


class GameBoard():

    def __init__(self, board_width: int, board_height: int) -> None:
        super().__init__()
        self.screen = Screen()

        self.screen.setup(width=board_width, height=board_height)
        self.screen.colormode(255)
        self.screen.bgcolor((0, 0, 0))
        self.screen.title(GAME_TITLE)
        self.screen.tracer(0)
        self.screen.listen()

        # Params

        self.board_width = board_width
        self.board_height = board_height
        self.board_x_max = board_width / 2
        self.board_x_min = 0 - self.board_x_max
        self.board_y_max = board_height / 2
        self.board_y_min = 0 - self.board_y_max

        self.computer_start_x = self.board_x_max - (2 * BLOCK_SIZE)
        self.player_start_x = 0 - self.computer_start_x
