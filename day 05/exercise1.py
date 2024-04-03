# LESSON 16 DAY 5 - AVERAGE HEIGHT

student_heights = input().split()
sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  sum += student_heights[n]

mean = sum / len(student_heights) 
mean_round = round(mean)
print(f"total height = {sum}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {mean_round}")
