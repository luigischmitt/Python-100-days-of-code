# NUMBER GUESSING GAME

from project_art import logo
from replit import clear
import random

def number_generator():
    return random.randint(1, 100)

def play_game():
    global number
    for _ in range(rounds):
        guess = int(input("Guess a number: "))
        if guess == number:
            print(f"You got it. The actual answer is {number}")
            return
        elif guess > number:
            print("Too high! Try again.")
        elif guess < number:
            print("Too low! Try again.")
    print("You've run out of guesses. You lose!")
    return False

while True: 
    clear()
    print(logo)
    print("Welcome to Number Guessing Game!")

    # Gera um novo número aleatório para cada iteração do loop
    number = number_generator()

    print("I am thinking in a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    if difficulty == "easy":
        rounds = 10
    elif difficulty == "hard":
        rounds = 5
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")
        continue

    if play_game(): # Se True
        play_again = input("Do you want to play again? Type 'yes' or 'no': ")
        if play_again.lower() != 'yes':
            print("Goodbye!")
            break
    else: # Se False
        play_again = input("Do you want to play again? Type 'yes' or 'no': ")
        if play_again.lower() != 'yes':
            print("Goodbye!")
            break
        