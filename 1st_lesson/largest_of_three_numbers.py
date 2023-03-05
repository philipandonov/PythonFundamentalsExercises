import sys

first_number = int(input())
second_number = int(input())
third_number = int(input())
biggest_number = -sys.maxsize
if first_number > second_number and first_number > third_number:
    biggest_number = first_number
elif second_number > first_number and second_number > third_number:
    biggest_number = second_number
else:
    biggest_number = third_number
print(biggest_number)