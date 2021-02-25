def logging_decorator(function):

    def wrapper(*args, **kwargs):
        
        log = f"Function called: {function.__name__}\n"
        
        if args:
            log += f"    arguments: {str(args)}\n"
        
        if kwargs:
            log += f"    kwargs: {str(kwargs)}\n"

        func_return = function(*args, **kwargs)

        log += f"    Return value: {func_return}\n\n"

        with open("log.txt", "a") as out:
            out.write(log)

        return func_return
    
    return wrapper


@logging_decorator
def a_function(num1, num2, num3):
    return num1 * num2 * num3


if __name__ == "__main__":
    result = [a_function(i, i+i, i+i+i) for i in range(1, 4)]
    print(result)

    result = [a_function(i, num2=i+i, num3=i+i+i) for i in range(1, 4)]
    print(result)

    result = [a_function(num1=i, num2=i+i, num3=i+i+i) for i in range(1, 4)]
    print(result)