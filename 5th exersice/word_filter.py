data = input().split()
filtered = [s for s in data if len(s) % 2 == 0]
print("\n".join(filtered))