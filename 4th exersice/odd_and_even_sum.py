def odd_even(string):
    even = 0
    odd = 0
    for current_num in string:
        current_number = int(current_num)
        if current_number % 2 == 0:
            even += current_number
        elif current_number % 2 != 0:
            odd += current_number
    return f"Odd sum = {odd}, Even sum = {even}"






number = input()
number_as_string = str(number)
print(odd_even(number_as_string))

