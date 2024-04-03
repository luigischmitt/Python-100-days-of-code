# Tip Calculator

print("Welcome to the tip calculator!")
total = float(input("Whats the total of the bill? $ "))
tip = float(input("How much tip would you like to give? (% 10, 12 or 15) "))
people = float(input("How many people will split the bill? "))

print("Each person should pay: ${:.2f}".format((total/people) * (100 + tip)/100))