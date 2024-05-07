with open("Python-100-days-of-code/day 24/studying about files/my_file.txt") as file: # We don't need to file.close() now
    contents = file.read()
    print(contents)

with open ("Python-100-days-of-code/day 24/studying about files/my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open ("Python-100-days-of-code/day 24/studying about files/new_file.txt", mode="w") as file:
    file.write("\nNew text.")
    