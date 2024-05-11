# LESSON 31 DAY 26 - DICTIONARY COMPREHENSION 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split(" ")

result = {word:len(word) for word in sentence}

print(result)
