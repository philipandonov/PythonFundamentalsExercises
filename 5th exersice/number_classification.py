data = list(map(int, (input().split(", "))))

positive = [str(s) for s in data if s >= 0]
negative = [str(s) for s in data if s < 0]
even = [str(s) for s in data if s % 2 == 0]
odd = [str(s) for s in data if s % 2 != 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
