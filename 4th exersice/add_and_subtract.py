def sum_numbers(some_numbers):
    return sum(some_numbers)


def subtract(first, second):
    return first - second


first_num = int(input())
second_num = int(input())
third_num = int(input())
all_nums = [first_num, second_num]
result_sum = sum_numbers(all_nums)
print(subtract(result_sum, third_num))
