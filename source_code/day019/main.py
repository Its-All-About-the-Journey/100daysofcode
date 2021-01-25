from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def forward():
	t.forward(20)


def backward():
	t.backward(20)


def cw():
	t.right(10)


def ccw():
	t.left(10)


def clear_and_center():
	s.reset()


s.listen()
s.onkeypress(key="w", fun=forward)
s.onkeypress(key="s", fun=backward)
s.onkeypress(key="d", fun=cw)
s.onkeypress(key="a", fun=ccw)
s.onkeypress(key="c", fun=clear_and_center)

s.exitonclick()



