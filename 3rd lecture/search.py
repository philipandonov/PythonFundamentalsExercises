number = int(input())
word = input()
whole_list = list()
filtered_list = list()
for i in range(number):
    string = input()
    whole_list.append(string)
    if word in string:
        filtered_list.append(string)
print(whole_list)
print(filtered_list)