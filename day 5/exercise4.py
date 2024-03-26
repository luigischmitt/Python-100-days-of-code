# LESSON 19 DAY 5 - FIZZBUZZ

for number in range(1, 101): # Include the number 100
  if (number % 3 == 0 and number % 5 == 0):
    print("FizzBuzz")
  elif (number % 3 == 0):
    print("Fizz")
  elif (number % 5 == 0):
    print("Buzz")
  else:
    print(number)
