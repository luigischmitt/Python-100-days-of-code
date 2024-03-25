print("\tWelcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Your ticket is $ 5.")
    elif age <= 18:
        bill = 7
        print("Your ticket is $ 7.")
    else:
        bill = 12
        print("Your ticket is $ 12.")

    wants_photo = str(input("Do you want a photo? Y or N. ")).strip().upper()
    if wants_photo == "Y":
        bill += 3
    else:
        bill += 0
    print(f"Your final bill is $ {bill}.")
    
else:
    print("Sorry, you have to grow taller before you can ride.")
