string = input().split(", ")
string_to_int_list = list(map(int, string))
index_list = []
for i, d in enumerate(string_to_int_list):
    if d % 2 == 0:
        index_list.append(i)
print(index_list)
