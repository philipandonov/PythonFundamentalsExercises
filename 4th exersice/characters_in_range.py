def get_char(first_char, second_char):
    collected_char = []
    for current_char in range(ord(first_character) + 1, ord(second_character)):
        collected_char.append(chr(current_char))
    return collected_char


first_character = input()
second_character = input()
result = get_char(first_character, second_character)
print(" ".join(result))
