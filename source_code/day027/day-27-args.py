#Function with any number of arguments (*args)

def add(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(add(5, 10, 15, 20, 2, 5))


def calculate(n, **kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(n + kwargs["add"])
    print(n * kwargs["multiply"])

calculate(2, add=3, multiply=5)

#Class with kwargs
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]
        
my_car = Car(make="Ford",model="Tempo")

print(my_car.model)

#Optional Kwargs
class Car2:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        
my_car = Car2(make="Ford", color="Red")

print(my_car.model)
print(my_car.color)


