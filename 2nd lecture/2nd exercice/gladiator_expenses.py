number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
total_helmet_broken = number_of_lost_fights // 2
total_sword_broken = number_of_lost_fights // 3
total_shield_broken = number_of_lost_fights // 6
total_armour_broken =  total_shield_broken // 2
expenses = total_armour_broken * armour_price + \
    total_shield_broken * shield_price + \
    total_sword_broken * sword_price + \
    total_helmet_broken * helmet_price
print(f"Gladiator expenses: {expenses:.2f} aureus")

