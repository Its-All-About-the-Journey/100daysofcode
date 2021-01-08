#Write your code below this line 👇

# In math, prime numbers are whole numbers greater than 1,
# that have only two factors – 1 and the number itself.
# Prime numbers are divisible only by the number 1 or itself.
# Source: https://www.splashlearn.com/math-vocabulary/algebra/prime-number

def prime_checker(number: int) -> None:

    # Assume true until proven false
    if number != 1:
        is_prime = True
    else:
        is_prime = False
    
    # Find proof it is not a prime number
    for n in range(2, number):
        if not (number % n):
            is_prime = False
            # Break out of for loop
            # We have proof
            break

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)