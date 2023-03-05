price_without_taxes = 0
taxes = 0

is_special = False
while True:
    command = input()
    if command == "special" or command == "regular":
        if command == "special":
            is_special = True
        break
    current_command = float(command)
    if current_command < 0:
        print("Invalid price!")
        continue
    price_without_taxes += current_command

taxes = price_without_taxes * 0.2
total_price = price_without_taxes + taxes
if is_special:
    total_price *= 0.9
if total_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_taxes:.2f}$\n"
      f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
