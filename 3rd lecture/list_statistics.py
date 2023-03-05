number = int(input())
negatives = list()
positives = list()
count_positives = 0
sum_of_negatives = 0
for i in range(number):
    current = int(input())
    if current >= 0:
        positives.append(current)
        count_positives += 1
    else:
        negatives.append(current)
        sum_of_negatives += current


print(positives)
print(negatives)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")