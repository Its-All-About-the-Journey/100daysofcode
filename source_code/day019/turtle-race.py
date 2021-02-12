from turtle import Turtle, Screen
import random
screen = Screen()
colors = ["Red", "Blue", "Green", "Purple", "Orange", "Yellow", "Brown", "Black", "Gray", "Beige"]
winner = ""

def draw_finish_line():
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.goto(300, 300)
    finish_line.pendown()
    finish_line.goto(300,-300)

def create_turtles(number_of_turtles):
    turtles = []
    for i in range(number_of_turtles):
        turtles.append(Turtle())
        turtles[i].shape("turtle")
        turtles[i].speed(10)
        turtles[i].color(colors[i].lower())
        turtles[i].penup()
        turtles[i].goto(-300,-250 + (i*50))
    return turtles

def start_race(guess):
    global turtles
    global winner
    race_over = False
    while race_over != True:
        for i in range(len(turtles)):
            turtles[i].forward(random.randint(0,10))
            winner = check_winner(turtles[i])
            if winner != "":
                print(f"You guessed the winner, {winner}!" if winner == guess else f"You guessed wrong, the winner is {winner}!")
                race_over = True

def check_winner(turtle):
    return str(turtle.color()[1]).capitalize() if int(turtle.xcor()) >= 300 else ""

turtles = create_turtles(int(screen.numinput("Number of racers","How many turtles are racing? (2-10): ", 5, minval=2, maxval=10)))
draw_finish_line()
guess = screen.textinput("Guess", "Who will win the race? (Enter a color): ")
start_race(guess)
screen.exitonclick()