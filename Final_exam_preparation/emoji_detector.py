import re

cool_threshold = 1
emoji = 0
stored_emoji = []
string = input()
pattern_1 = r"\d"
pattern_2 = r"(::|\*\*)([A-Z][a-z]{2,})\1"
matches_1 = re.findall(pattern_1, string)
if matches_1:
    for m in matches_1:
        cool_threshold *= int(m)
print(f"Cool threshold: {cool_threshold}")

matches_2 = re.finditer(pattern_2, string)
if matches_2:
    for match in matches_2:
        emoji += 1
        coolness = 0

        current_emoji = match.group(2)
        for ch in current_emoji:
            coolness += ord(ch)
        if coolness >= cool_threshold:
            stored_emoji.append(match.group(0))
print(f"{emoji} emojis found in the text. The cool ones are:")
for e in stored_emoji:
    print(e)
