starting_char = int(input())
final_char = int(input())
for char in range(starting_char, final_char + 1):
    current_char = chr(char)
    print(current_char,end= " ")