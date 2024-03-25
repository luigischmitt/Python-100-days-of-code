print("The Love Calculator is calculating your score...")
name1 = str(input("What is your name? ")).strip().lower()
name2 = str(input("What is their name? ")).strip().lower() 
both_names = name1 + name2

t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
first_digit = str(t + r + u + e)
l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")
e = both_names.count("e")
second_digit = str(l + o + v + e)

score = first_digit + second_digit
score_as_int = int(score)

if score_as_int < 10 or score_as_int > 90:
    print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int >= 40 and score_as_int <= 50:
    print(f"Your score is {score_as_int}, you are alright together.")
else:
    print(f"Your score is {score_as_int}.")