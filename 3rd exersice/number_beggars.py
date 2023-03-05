numbers = input().split(", ")
count_of_beggars = int(input())
beggars_taking_home = []
counter_of_index = 0
list_in_digits = []
final_list = []
for element in numbers:
    list_in_digits.append(int(element))
while counter_of_index < count_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(counter_of_index, len(list_in_digits), count_of_beggars):
        sum_of_current_beggar += list_in_digits[current_index]
    counter_of_index +=1
    final_list.append(sum_of_current_beggar)
print(final_list)