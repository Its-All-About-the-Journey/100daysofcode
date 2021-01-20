from turtle import Screen

class TurtleRaceView:
    
    def __init__(self, background: str):
        self.width = 500
        self.height = 400
        self.view_border = 10
        self.background = background
        self.view = Screen()
        self.setup_view()
    
    def setup_view(self):
        self.view.setup(
            width=self.width + self.view_border,
            height=self.height + self.view_border
        )

        self.view.colormode(255)
        self.view.bgcolor(self.background)

    def exitonclick(self):
        self.view.exitonclick()

    def text_input(self, title: str, prompt: str) -> str:
        return self.view.textinput(title, prompt)