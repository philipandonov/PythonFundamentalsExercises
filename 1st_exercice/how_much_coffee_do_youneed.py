command = input()
coffee = 0
while command != "END":
    if command == 'cat' or command == "dog" or command == "coding" or command == "movie":
        coffee += 1
    elif command == 'CAT' or command == "DOG" or command == "CODING" or command == "MOVIE":
        coffee += 2
    command = input()
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)