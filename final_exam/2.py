import re


n = int(input())
pattern = r"\|([A-Z]{4,})\|\:\#([A-Za-z]+\s[A-Za-z]+)\#"
for i in range(n):
    name = input()
    matches = re.finditer(pattern, name)
    is_matches = False
    if matches:
        for match in matches:
            is_matches = True
            boss = match.group(1)
            title = match.group(2)
            print(f"{boss}, The {title}")
            print(f">> Strength: {len(boss)}")
            print(f">> Armor: {len(title)}")
    if not is_matches:
        print("Access denied!")

