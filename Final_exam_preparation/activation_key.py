activation_key = input()
command = input()
while command != "Generate":
    current_command = command.split(">>>")
    if current_command[0] == "Contains":
        substring = current_command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif current_command[0] == "Flip":
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        if current_command[1] == "Upper":
            activation_key = activation_key[:start_index] + activation_key[
                                                            start_index:end_index].upper() + activation_key[end_index:]
            print(activation_key)
        elif current_command[1] == "Lower":
            activation_key = activation_key[:start_index] + activation_key[
                                                            start_index:end_index].lower() + activation_key[end_index:]
            print(activation_key)

    elif current_command[0] == "Slice":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")
