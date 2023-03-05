def minimum(list_of_nums):
    min_number = min(list_of_nums)
    return min_number


def maximum(list_of_nums):
    max_number = max(list_of_nums)
    return max_number


def suma(list_of_nums):
    sum_of_numbers = sum(list_of_nums)
    return sum_of_numbers

numbers = input().split()
str_to_digits = []
for i in numbers:
    str_to_digits.append(int(i))
print(f"The minimum number is {minimum(str_to_digits)}")
print(f"The maximum number is {maximum(str_to_digits)}")
print(f"The sum number is: {suma(str_to_digits)}")
