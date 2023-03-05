numbers = list(map(int, input().split(", ")))
max_number = max(numbers)
if max_number % 10 != 0:
    max_group = ((max_number // 10) + 1) * 10
else:
    max_group = (max_number // 10) * 10
x = 0
for group in range(10, max_group + 10, 10):
    current_list = []

    for s in numbers:
        if x < s <= group:
            current_list.append(s)
    x += 10
    print(f"Group of {group}'s: {current_list}")
