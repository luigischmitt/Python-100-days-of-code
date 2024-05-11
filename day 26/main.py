# Nato Phonetic Alphabet

import pandas as pd

df = pd.read_csv("Python-100-days-of-code/day 26/nato_phonetic_alphabet.csv")
nano_dict = {}

# TODO 1. Create a dictionary:
for (index, column) in df.iterrows():
    nano_dict[column.letter] = column.code

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = str(input("Input: ")).strip().upper()
name_list = [char for char in name]

for char in name_list:
    print(f"{char} for {nano_dict[char]}")
