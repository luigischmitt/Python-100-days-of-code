import random
import project_prints

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))
if (choice != 0 and choice != 1 and choice != 2):
    print("Invalid Input!")
computer_choice = random.randint(0, 2)

if (choice == 0 and computer_choice == 0):
    print(project_prints.rock)
    print("Computer chose:")
    print(project_prints.rock)
    print("It's a draw.")
elif (choice == 0 and computer_choice == 1):
    print(project_prints.rock)
    print("Computer chose:")
    print(project_prints.paper)
    print("You lose.")
elif (choice == 0 and computer_choice == 2):
    print(project_prints.rock)
    print("Computer chose:")
    print(project_prints.scissors)
    print("You win.")

if (choice == 1 and computer_choice == 1):
    print(project_prints.paper)
    print("Computer chose:")
    print(project_prints.paper)
    print("It's a draw.")
elif (choice == 1 and computer_choice == 0):
    print(project_prints.paper)
    print("Computer chose:")
    print(project_prints.rock)
    print("You win.")
elif (choice == 1 and computer_choice == 2):
    print(project_prints.paper)
    print("Computer chose:")
    print(project_prints.scissors)
    print("You lose.")

if (choice == 2 and computer_choice == 2):
    print(project_prints.scissors)
    print("Computer chose:")
    print(project_prints.scissors)
    print("It's a draw.")
elif (choice == 2 and computer_choice == 0):
    print(project_prints.scissors)
    print("Computer chose:")
    print(project_prints.rock)
    print("You lose.")
elif (choice == 2 and computer_choice == 1):
    print(project_prints.scissors)
    print("Computer chose:")
    print(project_prints.paper)
    print("You win.")
