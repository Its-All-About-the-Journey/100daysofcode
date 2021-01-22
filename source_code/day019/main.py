# 100 Days of Code: Python
# Day 19: Turtle Race
# Adam Pawlowski @hypermanaganate

from turtle import Turtle, Screen
from random import randint, choice

STEP_SIZE = 5
RESOLUTION_WIDTH = 500
RESOLUTION_HEIGHT = 400
ROY_G_BIV = {
    'red': (209, 0, 0),
    'orange': (255, 102, 34),
    'yellow': (255, 218, 33),
    'green': (51, 221, 0),
    'blue': (17, 51, 204),
    'indigo': (75, 0, 130),
    'violet': (51, 0, 68)
}

Y_BORDER = 50  # Can "compress" the turtles this way
X_BORDER = 10

X_MIN = 0 - (RESOLUTION_WIDTH / 2) + X_BORDER  # Minimum Y Coordinate
X_MAX = (RESOLUTION_WIDTH / 2) - X_BORDER  # Maximum X Coordinate
X_POS_INCREMENT = (abs(X_MIN) + X_MAX) / len(ROY_G_BIV)
X_POS_RELATIVE = X_POS_INCREMENT / 2  # Value to center from increment minimum

Y_MIN = 0 - (RESOLUTION_HEIGHT / 2) + Y_BORDER  # Minimum Y Coordinate
Y_MAX = (RESOLUTION_HEIGHT / 2) - Y_BORDER  # Maximum Y Coordinate
Y_POS_INCREMENT = (abs(Y_MIN) + Y_MAX) / len(ROY_G_BIV)
# Value of cellular spacing in Y axis
Y_POS_RELATIVE = Y_POS_INCREMENT / 2  # Value to center from increment minimum

LEADER_COMMENTARY = [
    '{leader} is out in front!',
    '{leader} has taken the lead!',
    '{leader} is now ahead!',
    'It looks like {leader} is pulling ahead!',
    "Oh my, it's now {leader} out front!"
    ]
OVERTAKE_COMMENTARY = [
    "They're leaving {previous} in the dust!",
    "Is {previous} running out of steam?",
    "Slow and steady isn't paying off for {previous}!"
    ]
MAINTAIN_COMMENTARY = [
    "{leader} is keeping ahead!",
    "Is {leader} going to run away with this one?",
    "This could be all over if {leader} pulls this off!"
]


class Racer:

    def __init__(self, color: str) -> 'Racer':
        super().__init__()
        self.race_car = Turtle()
        self.race_car.color(ROY_G_BIV[color])
        self.race_car.shape("turtle")
        self.race_car.pu()
        self.name = color
        self.x_pos = 0
        self.y_pos = 0

    def update_pos(self):
        self.x_pos = self.race_car.xcor()
        self.y_pos = self.race_car.ycor()

    def move_forward(self):
        self.race_car.forward(STEP_SIZE)

    def move_backward(self):
        self.race_car.backward(STEP_SIZE)

    def turn_left(self):
        self.race_car.right(10)

    def turn_right(self):
        self.race_car.left(10)

    def clear(self):
        self.race_car.pu()
        self.race_car.home()
        self.race_car.clear()
        self.race_car.pd()

    def go(self, coordinates: list):
        self.race_car.goto(coordinates[0], coordinates[1])
        self.update_pos()

    def walk(self, distance: int):
        self.race_car.pd()
        for _ in range(0, 1):
            if _ == 0:
                self.turn_right()
            else:
                self.turn_left()
            self.go([self.x_pos + (distance / 2), self.y_pos])
            self.update_pos()
            self.race_car.setheading(0)
        self.race_car.pu()


def setup_screen():
    """
    Setup Screen object for the game, and
    pass it back to the program for future use.
    """

    screen = Screen()
    screen.bgcolor("azure3")
    screen.setup(width=RESOLUTION_WIDTH, height=RESOLUTION_HEIGHT)
    screen.colormode(255)

    return screen


def check_leader(racer: Racer, leader_pos: int):
    if racer.x_pos > leader_pos:
        return [True, racer.x_pos]
    else:
        return [False, leader_pos]


def fire_commentary(leader: Racer, previous: Racer):
    if previous and previous != leader:
        _ = choice([0, 1])
        if _:
            print(choice(OVERTAKE_COMMENTARY).format(
                previous=previous.name.upper()))
    if previous and previous == leader:
        print(choice(MAINTAIN_COMMENTARY).format(leader=leader.name.upper()))
    else:
        print(choice(LEADER_COMMENTARY).format(leader=leader.name.upper()))


racers = []
leader = Racer

my_screen = setup_screen()

for num, color in enumerate(ROY_G_BIV):
    racers.append(Racer(color))

user_bet = ''

while user_bet not in ROY_G_BIV:
    user_bet = my_screen.textinput(title="Select a winner",
                                   prompt="Which turtle will win the race?" +
                                          "Enter a color:").lower()

print(f"You predict the {user_bet.upper()} turtle will win.\n" +
      "Good luck, and let's find out!\n")

starting_line = [X_MIN, Y_MIN]

for racer in racers:
    starting_line[1] += Y_POS_RELATIVE
    # print(f"Moving {racer.name} racer to {starting_line}")
    racer.go(starting_line)
    starting_line[1] += Y_POS_RELATIVE

are_racing = True
previous_leader = None
leader_pos = X_MIN
commentry_pos = X_MIN + X_POS_RELATIVE  # Inital Comment Trigger

print("And they're off!\n")

while are_racing:
    which_racer = choice(racers)
    how_far = randint(0, 11)
    which_racer.walk(how_far)
    is_leader, leader_pos = check_leader(which_racer, leader_pos)
    if is_leader and (leader_pos > commentry_pos):
        fire_commentary(which_racer, previous_leader)
        previous_leader = which_racer
        commentry_pos += X_POS_INCREMENT
    if leader_pos >= X_MAX:
        # Yes, the turtle can run off the canvas but it doesn't matter.
        are_racing = False
        print(f"\n...and it's the {which_racer.name.upper()}" +
              " turtle who takes the win!")

my_screen.exitonclick()
