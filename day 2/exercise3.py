age = input()

age_as_int = int(age)

weeks = int((4680 * age_as_int) / 90)
weeks_left = 4680 - weeks
print(f"You have {weeks_left} weeks left.")