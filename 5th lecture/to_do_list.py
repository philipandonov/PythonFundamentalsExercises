to_do = ['' for i in range(11)]
command = input()
while command != "End":
    com = command.split("-")
    index = int(com[0])
    thing_to_do = com[1]
    to_do[index] = thing_to_do
    command = input()
final_list = [i for i in to_do if i != ""]
print(final_list)
