#Write your code below this line 👇
def prime_checker(number):
    prime_flag = True
    if number > 1:
        for int in range(2,number):
            if number % int == 0:
                prime_flag = False
        if prime_flag:
            print(f"- {number} It's a prime number.")
        else:
            print(f"- {number} It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
