import re

some_string = input()
destinations = []
pattern = r"(\=|\/)([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, some_string)
for match in matches:
    destinations.append(match.group(2))
points = 0
for destination in destinations:
    points += len(destination)
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")