import random

from turtle import Turtle


class ObjectManager:
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    SHAPES = ["square", "turtle", "circle"]
    STARTING_MOVE_DISTANCE = 5
    MOVE_INCREMENT = 10
    MAX_WIDTH = 2.0

    def __init__(self) -> None:
        self.all_objects = list()
        self.object_move_step = self.STARTING_MOVE_DISTANCE

    def create_object(self) -> None:
        # Instantiate a Turtle and set properties with random values
        new_object = Turtle(random.choice(self.SHAPES))
        new_object.shapesize(stretch_wid=random.uniform(1.0, self.MAX_WIDTH))
        new_object.color(random.choice(self.COLORS))

        # Set object's state properties
        new_object.penup()
        new_object.setheading(180) # TODO: Pass heading in __init__
        random_y = random.randint(-250, 250) # TODO: Pass position boundaries in __init__
        new_object.setposition(300, random_y)

        # Add object to list of objects
        self.all_objects.append(new_object)

    def increase_speed(self) -> None:
        self.object_move_step += self.MOVE_INCREMENT * 0.2

    def move(self) -> None:
        for obj in self.all_objects:
            obj.forward(self.object_move_step)
