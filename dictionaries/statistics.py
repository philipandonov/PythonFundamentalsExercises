products = {}
counter = 0
while True:
    command = input()
    if command == "statistics":
        break
    current_products = command.split(": ")
    if current_products[0] not in products:
        products[current_products[0]] = int(current_products[1])
        counter += 1
    else:
        products[current_products[0]] += int(current_products[1])
product_representation = [f'- {item}: {str(current_products[0][item])}' for item in products]
print(f"Products in stock:)"
print(f"{'-'.join(products)}")
f"\n Total Products: {counter}\nTotal Quantity: {sum(products.values())}")