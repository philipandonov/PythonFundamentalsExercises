string = input()
command = input()
while command != "Done":
    current_command = command.split(" ")
    if current_command[0] == "Change":
        old_char = current_command[1]
        new_char = current_command[2]
        string = string.replace(old_char, new_char)
        print(string)
    elif current_command[0] == "Includes":
        if current_command[1] in string:
            print("True")
        else:
            print("False")
    elif current_command[0] == "End":
        list_of_strings = string.split()
        if current_command[1] in list_of_strings[-1]:
            print("True")
        else:
            print("False")
    elif current_command[0] == "Uppercase":
        string = string.upper()
        print(string)
    elif current_command[0] == "FindIndex":
        char = string.index(current_command[1])
        print(char)
    elif current_command[0] == "Cut":
        start_index = int(current_command[1])
        count = int(current_command[2])
        string = string[start_index:start_index + count]
        print(string)

    command = input()
