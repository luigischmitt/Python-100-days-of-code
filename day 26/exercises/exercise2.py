# LESSON 29 DAY 26 - FILTERING EVEN NUMBERS

list_of_strings = input().split(',')

list_of_int = [int(char) for char in list_of_strings]

result = [n for n in list_of_int if n % 2 == 0]

print(result)
