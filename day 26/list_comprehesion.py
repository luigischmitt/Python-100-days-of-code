# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

# name = "Luigi"
# new_list = [letter for letter in name]
# print(new_list)

# range_list = [n * 2 for n in range(1,5)]
# print(range_list)

# names = ["Dave", "Beth", "Angela", "Luigi", "Bia", "Tiago", "Marcus"]
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)

names = ["Dave", "Beth", "Angela", "Luigi", "Bia", "Tiago", "Marcus"]
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)
