secret_sentence = input().split()
filtered_list = []
for word in secret_sentence:
    number = int(''.join(x for x in word if x.isdigit()))
    letter = chr(number)
    new_word = ''
    for i in word:
        if i.isalpha():
            new_word += i
    new_word = letter + new_word
    word_list = [s for s in new_word]
    word_list[1], word_list[-1] = word_list[-1], word_list[1]
    final_word = ''.join(s for s in word_list)
    filtered_list.append(final_word)

print(" ".join(filtered_list))
