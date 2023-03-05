substrings = input().split(", ")
words = input().split(", ")
filtered_list = []
for sub in substrings:
    for word in words:
        if sub in word and sub not in filtered_list:
            filtered_list.append(sub)
print(filtered_list)
