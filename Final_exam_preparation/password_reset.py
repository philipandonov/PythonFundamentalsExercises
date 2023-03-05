string = input()
new_password = ''
command = input()
while command != "Done":
    current_command = command.split(" ")
    if current_command[0] == "TakeOdd":
        for i in range(1, len(string), 2):
            new_password += string[i]
        string = new_password
        print(new_password)
    elif current_command[0] == "Cut":
        index = int(current_command[1])
        length = int(current_command[2])
        string = string[:index] + string[index + length:]
        print(string)
    elif current_command[0] == "Substitute":
        substring = current_command[1]
        substitute = current_command[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {string}")