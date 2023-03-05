number_of_orders = int(input())
total = 0
for i in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100 or days < 1 or days > 31 or capsules_per_day < 1 or capsules_per_day > 2000:
        continue

    price = price_per_capsule * days * capsules_per_day
    total += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total:.2f}")
