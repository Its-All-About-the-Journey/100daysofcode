#Write your code below this line 👇

def prime_checker(number):
    prime = True
    for i in range(2, number-1):
        if number % i == 0:
            prime = False
            break
        
    print(f"{number} is a prime number." if prime else f"{number} is not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


