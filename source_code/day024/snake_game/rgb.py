from random import randint


def random_rgb_light():
	return randint(50, 255), randint(50, 255), randint(50, 255)


def random_rgb_pink():
	return 255, 0, randint(0, 255)
