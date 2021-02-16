from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
DIFFICULTY = {"easy": 9, "medium": 7, "hard": 5}

class CarManager():
    def __init__(self):
        self.cars = []
        self.pace = STARTING_MOVE_DISTANCE

    def create_car(self, choice):
        game_mode = random.randint(1, DIFFICULTY[choice])
        if game_mode == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.sample(COLORS,1))
            car.goto(random.randint(300,600), random.randint(-250,250))
            self.cars.append(car)

    def increase_speed(self):
        self.pace += MOVE_INCREMENT
             
    def move(self):
        for car in self.cars:
            car.backward(self.pace)