import re

total_calories = 0
matched = []
string = input()
pattern = r"(\#|\|)([A-Za-z\s]+)\1([0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(\d+)\1"
matches = re.finditer(pattern, string)
if matches:
    for match in matches:
        matched.append(match.group(2))
        matched.append(match.group(3))
        matched.append(match.group(4))

        total_calories += int(match.group(4))

total_days = total_calories / 2000
print(f"You have food to last you for: {int(total_days)} days!")
for first_match in range(0,len(matched), 3):
    print(f"Item: {matched[first_match]}, Best before: {matched[first_match+1]}, Nutrition: {matched[first_match+2]}")
