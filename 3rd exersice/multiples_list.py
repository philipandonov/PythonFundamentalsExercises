factor = int(input())
count = int(input())
numbers = []
for i in range(factor, (count * factor) + 1, factor):
    numbers.append(i)
print(numbers)
