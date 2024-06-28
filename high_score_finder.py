# in this program
# i am going highest score of the student in a classroom

#greeting
print("hello teacher!")

#taking input from teacher of student score
print("Enter below the students scores.")
students_score = input().split()
print(f"Students score = {students_score}")

for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])

highest_score = 0
for score in students_score:
    if score > highest_score :
        highest_score = score

print(f"Highest score = {highest_score}")
