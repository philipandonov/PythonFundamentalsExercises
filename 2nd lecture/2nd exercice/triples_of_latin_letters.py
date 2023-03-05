number_of_letters = int(input())
for char_1 in range(number_of_letters):
    for char_2 in range(number_of_letters):
        for char_3 in range(number_of_letters):
            print(f"{chr(97 + char_1)}{chr(97 + char_2)}{chr(97 + char_3)}")
