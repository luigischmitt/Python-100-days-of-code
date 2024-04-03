def prime_checker(number):
  div = 0
  for i in range(number):
    if number % (i + 1) == 0: # Can not be zero.
      div += 1
  if div == 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

n = int(input()) # Check this number
prime_checker(number=n)
