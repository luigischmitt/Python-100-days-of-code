# LESSON 30 DAY 26 - DATA OVERLAP

with open("Python-100-days-of-code/day 26/exercises/file1.txt") as file1:
    numbers = file1.readlines()
list1_int = [int(n) for n in numbers]

with open("Python-100-days-of-code/day 26/exercises/file2.txt") as file2:
    numbers = file2.readlines()
list2_int = [int(n) for n in numbers]

result = [n for n in list1_int if n in list2_int]

print(result)
