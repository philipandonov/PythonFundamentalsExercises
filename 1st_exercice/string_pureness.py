n = int(input())
for i in range(n):
    string = input()
    string_is_pure = True
    for c in string:
        if c == "_" or c == "," or c == ".":
            string_is_pure = False
            break
    if string_is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
