resources = {}
while True:
    current_resource = input()
    if current_resource == "stop":
        break
    quantity = int(input())
    if current_resource not in resources:
        resources[current_resource] = 0
    resources[current_resource] += quantity

for resource,quantity in resources.items():
    print(f"{resource} -> {quantity}")
