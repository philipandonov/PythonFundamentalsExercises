def electron_distribution(number):
    filled_list = []
    counter = 1
    while True:
        element = 2 * (counter ** 2)
        if element < number:
            number -= element
            filled_list.append(element)

        else:
            filled_list.append(number)
            break
        counter += 1
    print(filled_list)


number_of_electrons = int(input())
electron_distribution(number_of_electrons)
