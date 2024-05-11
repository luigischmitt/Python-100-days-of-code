import random

names = ["Dave", "Beth", "Angela", "Luigi", "Bia", "Tiago", "Marcus"]

# Looping through a list.
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# Looping through a dict.
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60} # dict.items()

print(passed_students)
