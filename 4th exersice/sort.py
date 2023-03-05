def sort(list):
    str_list_to_digits = []
    for i in list:
        str_list_to_digits.append(int(i))
    finished_list = sorted(str_list_to_digits)
    return finished_list


numbers = input().split()

print(sort(numbers))
