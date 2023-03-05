some_text = input()
new_text = ''
for i in range(len(some_text)):
    # if not some_text[i] in new_text:
    #     new_text += some_text[i]
    if i != (len(some_text) - 1):
        if some_text[i] == some_text[i + 1]:
            continue
        else:
            new_text += some_text[i]
    else:
        new_text += some_text[i]
print(new_text)
