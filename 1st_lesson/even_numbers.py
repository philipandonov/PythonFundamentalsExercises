n = int(input())
are_numbers_even = True
for i in range(1,n+1):
    number = int(input())
    if number % 2 != 0:
        are_numbers_even = False
        print(f"{number} is odd!")
        break

if are_numbers_even:
    print("All numbers are even.")
