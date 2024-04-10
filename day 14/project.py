# # HIGHER LOWER GAME

import random
from art import logo, vs
from game_data import data
from replit import clear

def check(A_followers, B_followers, score):
    answer = input("Who has more followers? Type 'A' or 'B': ").strip().upper()
    if answer == "A" and A_followers > B_followers:
        score += 1
        print(f"You're right! Current score: {score}")
        return score
    elif answer == "B" and B_followers > A_followers:
        score += 1
        print(f"You're right! Current score: {score}")
        return score
    else:
        print(f"Sorry, that's wrong! Final score: {score}")
        return False

def start_game():
    score = 0
    while True:
        clear()
        print(logo)
        print(f"Current score: {score}")

        # Escolher um item de A
        A_index = random.randint(0, len(data) - 1)
        A = data.pop(A_index)
        A_followers = A['follower_count']

        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
        print(vs)

        # Escolher um item de B
        B = random.choice(data)
        B_followers = B['follower_count']

        print("\n")
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
        score = check(A_followers, B_followers, score)
        if not score:
            break

start_game()