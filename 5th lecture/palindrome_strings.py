words = input().split(" ")
given_word = input()
palindromes = [i for i in words if i == i[::-1]]
count_of_given_word = 0
for word in palindromes:
    if given_word == word:
        count_of_given_word += 1
print(palindromes)
print(f"Found palindrome {count_of_given_word} times")
