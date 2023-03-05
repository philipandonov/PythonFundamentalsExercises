massage = input()
new_massage = massage
command = input()
while command != "Decode":
    current_command = command.split('|')
    the_command = current_command[0]
    if the_command == "Move":
        number_of_letters = int(current_command[1])
        for i in range(number_of_letters):
            current_massage = new_massage
            new_massage = current_massage[1:] + current_massage[0]
    elif the_command == 'Insert':
        index = int(current_command[1])
        value = current_command[2]
        string_in_list = [s for s in new_massage]
        string_in_list.insert(index, value)
        new_massage = "".join(string_in_list)
    elif the_command == 'ChangeAll':
        substring = str(current_command[1])
        replacement = str(current_command[2])

        new_massage = new_massage.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {new_massage}")
