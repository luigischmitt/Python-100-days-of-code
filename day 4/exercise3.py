import random

names = "Angela, Ben, Jenny, Michael, Chloe"
names_string = str(names)

names = names_string.split(", ")
lucky = random.randint(0, len(names) - 1)

print(f"{names[lucky]} is going to buy the meal today!")