# Python Decorator
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


@delay_decorator
def say_greeting():
    print("How are you?")


if __name__ == '__main__':
    say_hello()
    say_bye()
    say_greeting()