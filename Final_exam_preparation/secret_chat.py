

message = input()
command = input()
while command != "Reveal":
    data = command.split(':|:')
    current_command = data[0]
    if current_command == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]
    elif current_command == "Reverse":
        substring = data[1]
        if substring in message:
            message = message.replace(substring, "", 1) + substring[::-1]
        else:
            print("error")
            command = input()
            continue
    elif current_command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
    print(message)
    command = input()
print(f"You have a new text message: {message}")