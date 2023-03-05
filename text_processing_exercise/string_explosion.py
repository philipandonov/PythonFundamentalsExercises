some_text = input()
new_text = ''
strength = 0
for i in range(len(some_text)):
    if strength == 0 and some_text[i] != '>':
        new_text += some_text[i]
    elif strength > 0 and some_text[i] != '>':
        strength -= 1
        continue
    elif some_text[i] == '>':
        new_text += some_text[i]
        strength += int(some_text[i+1])
print(new_text)
