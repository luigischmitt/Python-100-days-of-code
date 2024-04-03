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

number1 = float(input("What's the first number? "))
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
number2 = float(input("What's the next number? "))

# 'operations[operation]' will be equal to add, sub, mul or div.
result = operations[operation](number1, number2)
print(f"{number1} {operation} {number2} = {result}")
