gifts = input().split()
command = input()
while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == current_gift:
                gifts[i] = "None"
    elif current_command[0] == "Required":
        i = int(current_command[2])
        if 0 <= i < len(gifts):
            gifts[i] = current_gift
    elif current_command[0] == "JustInCase":
        gifts[-1] = current_gift
    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end= " ")
        #gifts.remove(gift)
#x = " ".join(gifts)
#print(f"{x}")

