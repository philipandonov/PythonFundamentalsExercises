force_sides = {}
force_side_2 = {}

command = input()
while command != "Lumpawaroo":
    if "|" in command:
        current_command = command.split(" | ")
        force_side = current_command[0]
        force_user = current_command[1]
        present = False
        for value in force_sides.values():
            if force_user in value:
                present = True
                break
        if not present:
            if force_side not in force_sides:
                force_sides[force_side] = [force_user]
            else:
                force_sides[force_side].append(force_user)

    elif "->" in command:
        current_command = command.split(" -> ")
        force_user = current_command[0]
        force_side = current_command[1]

        for key, value in force_sides.items():
            if force_user in value:
                force_sides[key].pop(value.index(force_user))
                break
        if force_side not in force_sides:
            force_sides[force_side] = [force_user]
        else:
            force_sides[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")
    command = input()

for key in force_sides:
    if len(force_sides[key]) > 0:
        print(f"Side: {key}, Members: {len(force_sides[key])}")
        [print(f"! {user}") for user in force_sides[key]]
