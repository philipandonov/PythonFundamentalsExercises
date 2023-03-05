coffees = input().split()
number_of_commands = int(input())
for commands in range(number_of_commands):
    command = input().split()
    current_command = command[0]
    if current_command == "Include":
        coffees.append(command[1])
    elif current_command == "Remove" and int(command[2]) <= len(coffees):
        if command[1] == "first":
            for i in range(int(command[2])):
                coffees.pop(0)
        elif command[1] == "last":
            for i in range(int(command[2])):
                coffees.pop()
    elif current_command == "Prefer" and int(command[1]) <= len(coffees) - 1 and int(command[2]) <= len(coffees) - 1:
        coffees[int(command[1])] , coffees[int(command[2])] = coffees[int(command[2])] , coffees[int(command[1])]
    elif current_command == "Reverse":
        coffees.reverse()
print("Coffees:")
print(' '.join(s for s in coffees))