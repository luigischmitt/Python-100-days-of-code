def clear():  # #HINT: You can call clear() to clear the output in the console.
    print("\n" * 50)

from project_logo import logo

print(logo)

dictionary = {}

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $ "))
    
    dictionary[name] = bid

    another_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if another_bidder != 'yes':
        break
    else: 
        clear()
        print(logo)

highest = 0

for name in dictionary:
    if dictionary[name] > highest:
        winner = name
        highest = dictionary[name]

print(f"The winner is {winner} with a bif of $ {highest}") 