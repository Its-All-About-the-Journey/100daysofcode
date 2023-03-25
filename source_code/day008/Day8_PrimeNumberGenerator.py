def prime_checker(number):
  if number > 1:
    for x in range(2, number):
      if number % x == 0:
        return False
    return True
  else:
    return False

    
n = int(input("Check this number: "))
#if prime_checker(number=n):
#  print(f"{n} is a prime number")
#else:
#  print(f"{n} is not a prime number")
    
primenums = []
for x in range(2, n):
  if prime_checker(number=x):
    primenums.append(x)
#  else:
#    print(f"{n} is not a prime number")
print(primenums)