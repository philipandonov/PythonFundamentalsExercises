string = input()
digits = [d for d in string if d.isdigit()]
letters = [l for l in string if l.isalpha()]
others = [s for s in string if not s.isalnum()]
print("".join(digits))
print("".join(letters))
print("".join(others))