list_of_numbers = input().split()
count_of_num_to_remove = int(input())
removed_num = 0

filtered_list = []
copy_filtered_list = []
for i in list_of_numbers:
    filtered_num = int(i)
    filtered_list.append(filtered_num)
    copy_filtered_list.append(filtered_num)
filtered_list.sort()

for num in filtered_list:
    if removed_num >= count_of_num_to_remove:
        break
    copy_filtered_list.remove(num)
    removed_num += 1
for i in copy_filtered_list:
    if i == copy_filtered_list[-1]:
        print(i, end="")
    else:
        print(i, end=", ")
