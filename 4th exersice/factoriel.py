def factorial(number):
    for factorial in range(1, number):
        number *= factorial
    return number


first_num = int(input())
second_num = int(input())
first_number_factorial = factorial(first_num)
second_number_factorial = factorial(second_num)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")