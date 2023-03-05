number_of_pieces = int(input())
my_collection = {}
for i in range(number_of_pieces):
    pieces = input().split('|')
    key = pieces[0]
    author = pieces[1]
    notes = pieces[2]
    my_collection[key] = [author, notes]
while True:
    command = input()
    if command == 'Stop':
        break
    current_command = command.split('|')
    choice = current_command[0]
    if choice == 'Add':
        piece = current_command[1]
        composer = current_command[2]
        key = current_command[3]
        if not piece in my_collection.keys():
            my_collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    if choice == "Remove":
        piece = current_command[1]
        if not piece in my_collection.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            my_collection.pop(piece)
            print(f"Successfully removed {piece}!")
    if choice == "ChangeKey":
        piece = current_command[1]
        new_key = current_command[2]
        if not piece in my_collection.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            my_collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

for key,value in my_collection.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")