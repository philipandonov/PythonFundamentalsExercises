courses = {}
command = input()
while command != "end":
    course_name, student = command.split(" : ")
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student)
    command = input()
for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for s in value:
        print(f"-- {s}")