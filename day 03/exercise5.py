print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
bill = 0

if size == "S" and add_pepperoni == "N":
  bill = 15
elif size == "S" and add_pepperoni == "Y":
  bill = 17
elif size == "M" and add_pepperoni == "N":
  bill = 20
elif size == "M" and add_pepperoni == "Y":
  bill = 23
elif size == "L" and add_pepperoni == "N":
  bill = 25
elif size == "L" and add_pepperoni == "Y":
  bill = 28
else:
  bill += 0

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")