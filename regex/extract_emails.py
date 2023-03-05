import re

emails = input()
pattern = r"((?<=\s)([a-z0-9]+[\.\-\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)"
matches = re.findall(pattern, emails)


for match in matches:
    print(match[0])