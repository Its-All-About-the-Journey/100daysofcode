for n in range(1,101):
  if n % 3 == 0 and n % 5 == 0:
    print("Fizz Buzz")
  elif n % 5 == 0:
    print("Buzz")
  elif n % 3 == 0:
    print("Fizz")
  else:
    print(n)
    