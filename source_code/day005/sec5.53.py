
# 3 5
# T T - FB
# T F - F 
# F T - B
# F F - num

for i in range(1, 101):
    # if divisible then not(0)
    is_fizz = not(i % 3)
    is_buzz = not(i % 5)

    if is_fizz and is_buzz:
        print('FizzBuzz')
    
    elif is_fizz:
        print('Fizz')
    
    elif is_buzz:
        print('Buzz')
    
    else: # is num
        print(i)
