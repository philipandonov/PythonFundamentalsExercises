first_command = input()
cities = {}
while first_command != "Sail":
    town, population, gold = first_command.split("||")
    if town in cities:
        cities[town]['population'] += int(population)
        cities[town]['gold'] += int(gold)
    else:
        cities[town] = {'population': int(population), 'gold': int(gold)}
    first_command = input()

command = input()
while command != 'End':
    current_command = command.split("=>")
    if current_command[0] == 'Plunder':
        town = current_command[1]
        people = int(current_command[2])
        gold = int(current_command[3])
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
    elif current_command[0] == 'Prosper':
        town = current_command[1]
        gold = int(current_command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            command = input()
            continue
        else:
            cities[town]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

    command = input()
if cities == {}:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f"{city} -> Population: {cities[city]['population']} citizens, Gold: {cities[city]['gold']} kg")
