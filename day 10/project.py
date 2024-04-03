from tracemalloc import stop
from project_art import logo

print(logo)

def add(number1, number2):
    return number1 + number2
def sub(number1, number2):
    return number1 - number2
def mul(number1, number2):
    return number1 * number2
def div(number1, number2):
    return number1 / number2

# Creating a dictionary:
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

should_continue = True

number1 = float(input("What's the first number? "))
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
number2 = float(input("What's the next number? "))

# 'operations[operation]' will be equal to add, sub, mul or div.
result = operations[operation](number1, number2)
print(f"{number1} {operation} {number2} = {result}")

while should_continue == True:
    stop = str(input("Type 'y' to continue calculating with the result, or type 'n' to exit: ")).strip().lower()
    if stop == "n":
        print("Good bye!")
        should_continue = False
    else:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        aux = float(input("What's the next number? "))
        new_result = operations[operation](result, aux)
        print(f"{result} {operation} {aux} = {new_result}")
        result = new_result