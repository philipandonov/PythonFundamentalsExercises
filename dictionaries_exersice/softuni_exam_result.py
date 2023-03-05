submission = {}
results = {}
command = input()
while command != "exam finished":
    current_command = command.split("-")
    username = current_command[0]
    language = current_command[1]
    if len(current_command) == 3:
        points = int(current_command[2])

    if username not in results.keys():
        results[username] = points
    else:
        if results[username] < points:
            results[username] = points
        if language == "banned":
            results.pop(username)
    if language != "banned":
        if language not in submission:
            submission[language] = 1
        else:
            submission[language] += 1
    command = input()
print("Results:")
for key, value in results.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in submission.items():
    print(f"{key} - {value}")
