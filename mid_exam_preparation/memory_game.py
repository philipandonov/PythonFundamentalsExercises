def hit_elements(first_ind, second_ind):
    if sequence_of_elements[first_ind] == sequence_of_elements[second_ind]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_ind]}!")

        sequence_of_elements.remove(sequence_of_elements.pop(first_ind))

    else:
        print("Try again!")


sequence_of_elements = input().split()
move_counter = 0
is_win = False
while True:
    command = input()
    if command == "end":
        break
    move_counter += 1
    current_command = list(map(int, command.split()))
    first_index = current_command[0]
    second_index = current_command[1]
    if first_index < 0 or first_index >= len(sequence_of_elements) or second_index < 0 or second_index >= len(
            sequence_of_elements) or first_index == second_index:
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{move_counter}a")
        sequence_of_elements.insert(int(len(sequence_of_elements) / 2), f"-{move_counter}a")
        print("Invalid input! Adding additional elements to the board")
        continue
    hit_elements(first_index, second_index)
    if len(sequence_of_elements) == 0:
        is_win = True
        break

if is_win:
    print(f"You have won in {move_counter} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
