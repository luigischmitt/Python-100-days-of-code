# Caeser Cipher

from project_logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False

while should_end == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)    
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")

    def decrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)    
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The decoded text is {cipher_text}")

    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(plain_text=text, shift_amount=shift)
    else: 
        print("Invalid input. You need to chose 'encode' or 'decode'.")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye!")