number = int(input())
wagoon_list = [0 for i in range(number)]

command = input()

while command != "End":
    com = command.split()
    operation = com[0]
    if operation == "add":
        wagoon_list[-1] += int(com[1])
    if operation == "insert":
        index = int(com[1])
        wagoon_list[index] += int(com[2])
    if operation == "leave":
        index = int(com[1])
        wagoon_list[index] -= int(com[2])

    command = input()
print(wagoon_list)