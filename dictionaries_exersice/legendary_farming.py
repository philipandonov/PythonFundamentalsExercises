points = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
command = input().split()
while True:
    for i in range(0, len(command), 2):
        key = command[i + 1].lower()
        value = int(command[i])
        if key in points:
            points[key] += value
        else:
            points[key] = value
        if points["shards"] >= 250:
            print("Shadowmourne obtained!")
            points["shards"] -= 250
            obtained = True
        elif points["fragments"] >= 250:
            print("Valanyr obtained!")
            points["fragments"] -= 250
            obtained = True
        elif points["motes"] >= 250:
            print("Dragonwrath obtained!")
            points["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

    command = input().split()
for key, value in points.items():
    print(f"{key}: {value}")
