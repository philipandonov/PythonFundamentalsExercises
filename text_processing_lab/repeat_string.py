string = ''
words = input().split()
for i in range(len(words)):
    string += words[i] * len(words[i])
print(string)
