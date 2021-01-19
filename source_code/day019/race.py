from random import randint
from turtle import Turtle, Screen
screen = Screen()
screen.colormode(255)

# t1 = Turtle()
#
#
# def move_forwards():
#     t1.forward(5)
#
#
# def move_backwards():
#     t1.backward(5)
#
#
# def rotate_ccw():
#     t1.left(5)
#
#
# def rotate_cw():
#     t1.right(5)
#
#
# def clear_drawing():
#     screen.reset()
#
#
# screen.onkeypress(move_forwards, "w")
# screen.onkeypress(move_backwards, "s")
# screen.onkeypress(rotate_ccw, "a")
# screen.onkeypress(rotate_cw, "d")
# screen.onkey(clear_drawing, "c")


screen.setup(width = 500, height = 400)
racers = [Turtle(shape = "turtle") for _ in range(7)]
starting_line = -222
finish_line = 222
spacing = 30


def rand_color():
    r = randint(1, 255)
    g = randint(1, 255)
    b = randint(1, 255)
    return (r, g, b)


def lineup():
    center = 0 if len(racers) % 2 > 0 else spacing / 2 * -1
    lane = len(racers) // 2 * spacing + center
    for racer in racers:
        racer.penup()
        racer.color(rand_color())
        racer.goto(x = starting_line, y = lane)
        lane -= spacing
        
        
def start_race():
    race_over = False
    
    # run the race until someone wins
    while not race_over:
        
        # incrementally move each racers forward by some amount, and then check to see if they crossed the finish line
        for racer_number in range(len(racers)):
            
            # 0.01% chance of boosting when we execute order 66
            if randint(1, 10_000) == 66:
                increment_by = 66
                
            # else just let them run at their normal pace
            else:
                increment_by = randint(1, 2)
                
            # make sure we don't over shoot the finish line
            if racers[racer_number].xcor() + increment_by > finish_line:
                racers[racer_number].goto(x = finish_line, y = racers[racer_number].ycor())
            else:
                racers[racer_number].forward(increment_by)
                
            # did someone win?
            if racers[racer_number].xcor() >= finish_line:
                winner = racer_number + 1
                race_over = True
                break
                
    return winner
                

lineup()
users_bet = screen.textinput(title = "Make your bet!", prompt = "Which turtle will win the race? Enter #: ")
winner = start_race()
screen.textinput(title = "Race Complete", prompt = f"The winner is racer #{winner}!")
screen.listen()
screen.exitonclick()