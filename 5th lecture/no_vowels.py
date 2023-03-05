list_of_vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
no_vowels = "".join([letter for letter in text if letter not in list_of_vowels])
print(no_vowels)
