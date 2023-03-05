products = {}
command = input()
while command != "buy":
    name_of_product, price, quantity = command.split()
    if name_of_product not in products:
        products[name_of_product] = [float(price), int(quantity)]
    else:
        products[name_of_product][0] = float(price)
        products[name_of_product][1] += int(quantity)

    command = input()

for product in products:
    total_price = products[product][0] * products[product][1]
    print(f"{product} -> {total_price:.2f}")
