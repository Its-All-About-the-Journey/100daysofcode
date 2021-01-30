# 100 Day of Code: Python
# Not Frogger: Main Game
# Adam Pawlowski (@hypermanganate)

from turtle import Turtle, TurtleScreen
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_LEFT = 280
START_RIGHT = -280


def setup_car_shapes(screen: TurtleScreen):
    for color in COLORS:
        screen.register_shape(f"assets/car_{color}_left.gif")
        screen.register_shape(f"assets/car_{color}_right.gif")


class Car(Turtle):
    def __init__(self, start_y: float, speed: int) -> None:
        super().__init__()
        self.pu()
        self.reset(start_y)
        self.speed = speed

    def move(self):
        self.forward(MOVE_INCREMENT * self.speed)
        if self.direction == "left" and self.xcor() < self.end_position:
            return False
        if self.direction == "right" and self.xcor() > self.end_position:
            return False
        else:
            return True

    def reset(self, start_y: int):
        self.setheading(choice([0.0, 180.0]))
        if self.heading() == 180.0:
            self.direction = "left"
            self.setposition(START_LEFT, start_y)
            self.end_position = -1 * START_LEFT
        else:
            self.direction = "right"
            self.setposition(START_RIGHT, start_y)
            self.end_position = -1 * START_RIGHT
        self.shape(f"assets/car_{choice(COLORS)}_{self.direction}.gif")

    def set_speed(self, car_speed: int):
        car_speed_scale = choice(list(range(5, 11)))
        car_speed_scale = car_speed_scale / 10
        self.speed = car_speed * car_speed_scale


class CarManager:
    def __init__(self, num_cars: int, car_speed: int, field_y_min: int,
                 field_y_max: int) -> None:
        """
        Create a new car manager.

        Specify the number of starting cars (num_cars)
        Specify the starting speed (car_speed)
        Field Y Min/Max represents the area cars can appear in
        """

        self.cars = []
        self.y_min = field_y_min
        self.y_max = field_y_max
        self.num_cars = num_cars
        for _ in range(self.num_cars):
            self.add_car(car_speed)

    def check_for_accidents(self, player_position: tuple):
        for car in self.cars:
            if abs(car.ycor() - player_position[1]) < 20:
                if abs(car.xcor() - player_position[0]) < 20:
                    return True

        return False

    def get_car_positions(self):
        positions = []

        for car in self.cars:
            positions.append(car.ycor())

        return positions

    def get_car_position(self) -> float:
        """
        Return a car position.
        """

        position = choice(list(range(self.y_min, self.y_max, 40)))
        while position in self.get_car_positions():
            position = choice(list(range(self.y_min, self.y_max, 40)))

        return position

    def move_cars(self):
        for car in self.cars:
            if not car.move():
                car.reset(self.get_car_position())

    def set_level(self, level: int):
        for car in self.cars:
            car.set_speed(level)
            car.reset(self.get_car_position())

    def add_car(self, speed: int = 1):
        car_speed_scale = choice(list(range(5, 11)))
        car_speed_scale = car_speed_scale / 10
        self.cars.append(Car(self.get_car_position(),
                         speed=car_speed_scale * speed))
