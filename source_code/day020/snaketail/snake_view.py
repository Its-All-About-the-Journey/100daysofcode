from turtle import Screen

from snaketail.snake_defaults import SnakeDefaults as CFG

class SnakeView:

    def __init__(self):
        self.screen = Screen()
        self.init_screen()

    def init_screen(self):
        self.screen.setup(width=CFG.SCREEN["width"], height=CFG.SCREEN["height"])
        self.screen.bgcolor(CFG.SCREEN["bgcolor"])
        self.screen.title(CFG.SCREEN["title"])
        self.screen.tracer(CFG.SCREEN["tracer"])
    
    def update(self):
        self.screen.update()