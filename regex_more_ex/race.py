import re

list_of_names = input().split(', ')

pattern = r"[A-Za-z]"
pattern_2 = r"\d"
names_dict = {}
string = input()
while string != "end of race":
    matches = re.findall(pattern, string)
    matches_2 = re.findall(pattern_2, string)
    if matches:
        name = "".join(matches)

        distance = sum(map(int, matches_2))

        if name in list_of_names:
            if name not in names_dict:
                names_dict[name] = distance
            else:
                names_dict[name] += distance

    string = input()

new_dict = sorted(names_dict.items(), key=lambda x: x[1], reverse=True)

number = 0
for i in new_dict:
    number += 1
    if number >3:
        break
    if number == 1:
        print(f"1st place: {i[0]}")
    elif number == 2:
        print(f"2nd place: {i[0]}")
    elif number == 3:
        print(f"3rd place: {i[0]}")