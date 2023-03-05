number_of_actions = int(input())
plants_information = {}
for i in range(number_of_actions):
    plants = input().split('<->')
    plant, rarity = plants
    plants_information[plant] = {'rarity': int(rarity), 'rating': []}

command = input()
while command != "Exhibition":
    current_command = command.split(": ")
    take_plant_rating = current_command[1].split(" - ")
    plant = take_plant_rating[0]
    if plant in plants_information:
        if current_command[0] == "Rate":
            rating = int(take_plant_rating[1])
            plants_information[plant]['rating'].append(rating)
        elif current_command[0] == "Update":
            new_rarity = int(take_plant_rating[1])

            plants_information[plant]["rarity"] = new_rarity
        elif current_command[0] == "Reset":
            plants_information[plant]["rating"] = []
    else:
        print("error")
    command = input()
print("Plants for the exhibition:")
for plant in plants_information:
    if len(plants_information[plant]["rating"]) != 0:
        average_rating = sum(plants_information[plant]["rating"])/len(plants_information[plant]["rating"])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {plants_information[plant]['rarity']}; Rating: {average_rating:.2f}")

