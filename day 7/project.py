# THE HANGMAN GAME

import random
from project_prints import stages, logo
from project_words import word_list

print(logo) 

chosen_word = random.choice(word_list)
display = []

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

for i in range (len(chosen_word)):
    display.append("_")

wrong = False
lives = 6

while "_" in display:
    if lives == 0:
        print("You lose!")
        break
    guess = str(input("Guess a letter: ")).strip().lower()
    if guess in display:
        print("You already chose this letter. Try again.")
    for i in range (len(chosen_word)):
        if guess in chosen_word[i]:
            display[i] = guess
            wrong = False
        elif guess not in chosen_word:
            wrong = True
    if wrong is True:
        print("This letter is not in the word. You lose a life!")
        lives -= 1
        print(stages[lives])
    else:
        lives -= 0
        print(stages[lives])
    print("".join(display))

if lives > 0:
    print("You win!")