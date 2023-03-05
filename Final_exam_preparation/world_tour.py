destination = input()

command = input()
while True:
    if command == "Travel":
        break
    current_command = command.split(":")
    stop = current_command[0]
    if stop == "Add Stop":
        index = int(current_command[1])
        string = current_command[2]
        if 0 <= index < len(destination):
            destination = destination[:index] + string + destination[index:]
        print(destination)
    if stop == "Remove Stop":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        if 0 <= start_index < len(destination) and 0 <= end_index < len(destination):
            destination = destination[:start_index] + destination[end_index+1:]
        print(destination)
    if stop == "Switch":
        old_string = current_command[1]
        new_string = current_command[2]
        if old_string in destination:
            destination = destination.replace(old_string, new_string)
        print(destination)

    command = input()
print(f"Ready for world tour! Planned stops: {destination}")
