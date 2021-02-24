import time


def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        function()
        final_time = time.time() - start_time
        print(f"{function.__name__} run speed: {final_time:.4f} secs")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


if __name__ == '__main__':
    slow_function()
    fast_function()