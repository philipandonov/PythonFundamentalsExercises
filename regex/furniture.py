import re

command = input()
pattern = r">{2}([A-Za-z]+)<<(\d+\.?\d*)!(\d)"
total_cost = 0
bought_furniture = []
while command != "Purchase":

    matches = re.search(pattern, command)
    if matches:
        furniture , price, quantity = matches.groups()
        bought_furniture.append(furniture)
        total_cost += int(quantity) * float(price)

    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")