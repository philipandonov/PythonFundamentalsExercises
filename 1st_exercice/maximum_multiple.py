number = int(input())
boundary = int(input())
for i in range(boundary, number - 1, -1):
    if i % number == 0:
        print(i)
        break
