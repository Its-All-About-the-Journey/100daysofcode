def add(*args):
	print(*args)
	print(args)
	return sum(args)


print(add(2, 4, 6, 8, 10))


def calculate(n, **kwargs):
	print(kwargs)
	n += kwargs['add']
	n *= kwargs['multiply']
	return n


print(calculate(2, add=3, multiply=5))
