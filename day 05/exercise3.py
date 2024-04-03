# LESSON 18 DAY 5 - ADDING EVEN NUMBERS

target = int(input()) # Enter a number between 0 and 1000

sum = 0
for number in range(0, target + 1, 2):
  sum += number

print(sum)