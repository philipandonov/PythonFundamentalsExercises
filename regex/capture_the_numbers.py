import re

pattern = r"\d+"
string = input()
while True:
    if string:
        match = re.findall(pattern, string)
        if match:
            print(" ".join(match), end=" ")
        string = input()
    else:
        break


