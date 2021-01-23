from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
t.shape("turtle")
screen.colormode(255)
screen.bgcolor("white")


def random_rgb():
	return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_shapes():
	t.shape("arrow")
	move_size = 100
	for i in range(3, 10):
		t.pencolor(random_rgb())
		for _ in range(i):
			t.forward(move_size)
			t.right(360/i)


def random_walk():
	t.shape("circle")
	t.hideturtle()
	t.speed(20)
	t.pensize(15)
	move_size = 30
	for _ in range(200):
		t.pencolor(random_rgb())
		turn_angle = random.choice([0, 90, 180, 270])
		if turn_angle == 270:
			t.left(90)
		else:
			t.right(turn_angle)
		t.forward(move_size)


def draw_spiro():
	t.shape('arrow')
	t.speed('fastest')
	t.pensize(4)
	t.hideturtle()
	degrees_of_separation = 10
	executions = int(360/degrees_of_separation)
	for _ in range(executions):
		t.pencolor(random_rgb())
		t.circle(200)
		t.right(degrees_of_separation)


draw_spiro()
draw_shapes()
random_walk()


screen.exitonclick()
