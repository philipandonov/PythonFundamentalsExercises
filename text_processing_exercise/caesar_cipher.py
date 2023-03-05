text = input()
new_text = ''
for letter in text:
    new_text += chr(ord(letter) + 3)
print(new_text)
