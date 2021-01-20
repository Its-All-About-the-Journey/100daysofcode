from turtle import Turtle, Screen

from .key_binding import KeyBindings as kb

class EtchSketch:

    def __init__(self):
        self.tim = Turtle()
        self.view = Screen()
        self.defaults = dict()

        self.view.listen()
        self.load_key_bindings()

    def forward(self):
        self.tim.forward(self.defaults["forward"])

    def backward(self):
        self.tim.backward(self.defaults["backward"])

    def clear(self):
        self.tim.clear()
        self.tim.penup()
        self.tim.home()
        self.tim.pendown()

    def clockwise(self):
        heading = self.tim.heading() + self.defaults["clockwise"]
        self.tim.setheading(heading)

    def counter_clockwise(self):
        heading = self.tim.heading() + self.defaults["counter_clockwise"]
        self.tim.setheading(heading)

    def load_key_bindings(self):
        for key in kb.key_events:
            function = kb.key_events[key]["function"]
            self.view.onkey( key=key, fun=getattr(self, function) )

            # Set default values for each function
            if kb.key_events[key]["amount"]:
                self.defaults[function] = kb.key_events[key]["amount"]
    
    def run(self):
        self.view.exitonclick()