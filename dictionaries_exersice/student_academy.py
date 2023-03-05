students = {}
number = int(input())
for current_student in range(number):
    name_of_student = input()
    grade = float(input())
    if name_of_student not in students:
        students[name_of_student] = []
    students[name_of_student].append(grade)


for key, value in students.items():
    average_grade = sum(value) / len(value)
    if average_grade >= 4.5:
        print(f"{key} -> {average_grade:.2f}")
