number_of_days_for_adventure = int(input())
number_of_players = int(input())
energy_of_the_group = float(input())
water_for_a_person_for_day = float(input())
food_for_a_person_for_day = float(input())
total_water_for_adventure = water_for_a_person_for_day * number_of_days_for_adventure * number_of_players
total_food_for_adventure = food_for_a_person_for_day * number_of_days_for_adventure * number_of_players
days_counter = 1
is_end = True
while days_counter <= number_of_days_for_adventure:

    current_lost_of_energy = float(input())
    energy_of_the_group -= current_lost_of_energy
    if energy_of_the_group <= 0:
        is_end = False
        print(
            f"You will run out of energy. You will be left with {total_food_for_adventure:.2f} food and {total_water_for_adventure:.2f} water.")
        break
    if days_counter % 2 == 0:
        energy_of_the_group += 0.05 * energy_of_the_group
        total_water_for_adventure -= 0.3 * total_water_for_adventure
        if energy_of_the_group <= 0:
            is_end = False
            print(
                f"You will run out of energy. You will be left with {total_food_for_adventure:.2f} food and {total_water_for_adventure:.2f} water.")
            break
    if days_counter % 3 == 0:
        total_food_for_adventure -= total_food_for_adventure / number_of_players
        energy_of_the_group += 0.1 * energy_of_the_group
        if energy_of_the_group <= 0:
            is_end = False
            print(
                f"You will run out of energy. You will be left with {total_food_for_adventure:.2f} food and {total_water_for_adventure:.2f} water.")
            break

    days_counter += 1

if is_end:
    print(f"You are ready for the quest. You will be left with - {energy_of_the_group:.2f} energy!")
