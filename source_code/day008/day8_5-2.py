def prime_checker(number):
    prime = False
    for num in range(2, number):
        if number % num == 0:
            prime = True
    if prime:
        print("It's not a prime number")
    else:
        print("It's a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)