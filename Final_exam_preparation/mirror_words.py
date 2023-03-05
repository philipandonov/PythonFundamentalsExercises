import re

stored_words = []
counter_of_pairs = 0
string = input()
pattern = r"(\#|\@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.finditer(pattern, string)
if matches:
    for match in matches:
        counter_of_pairs += 1

        if match.group(2) == match.group(3)[::-1]:
            stored_words.append(match.group(2))
            stored_words.append(match.group(3))
finished = []
if counter_of_pairs == 0:
    print("No word pairs found!")
else:
    print(f"{counter_of_pairs} word pairs found!")
if len(stored_words) != 0:
    print("The mirror words are:")
    for i in range(0, len(stored_words), 2):
        mirror_words = f"{stored_words[i]} <=> {stored_words[i+1]}"
        finished.append(mirror_words)
    print(f"{', '.join(finished)}")
else:
    print(f"No mirror words!")

