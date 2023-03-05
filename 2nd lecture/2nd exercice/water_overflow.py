number_of_times_filling = int(input())
capacity = 255
litters_to_tank = 0
for i in range(number_of_times_filling):
    current_litters = int(input())
    if current_litters + litters_to_tank > capacity:
        print("Insufficient capacity!")
        continue
    litters_to_tank += current_litters
print(litters_to_tank)
