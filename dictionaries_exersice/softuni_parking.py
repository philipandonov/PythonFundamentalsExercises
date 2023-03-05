number_of_commands = int(input())
parking_users = {}
for n in range(number_of_commands):
    command = input().split()
    current_command = command[0]
    user = command[1]

    if current_command == "register":
        number = command[2]
        if user in parking_users:
            print(f"ERROR: already registered with plate number {number}")
        else:
            parking_users[user] = number
            print(f"{user} registered {number} successfully")
    elif current_command == "unregister":
        if user not in parking_users:
            print(f"ERROR: user {user} not found")
        else:
            parking_users.pop(user)
            print(f"{user} unregistered successfully")

for user, number in parking_users.items():
    print(f"{user} => {number}")

