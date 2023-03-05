command = input()
is_welcome = True
while command != "Welcome!":
    if command == "Voldemort":
        is_welcome = False
        print("You must not speak of that name!")
        break
    if len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()
if is_welcome:
    print("Welcome to Hogwarts.")