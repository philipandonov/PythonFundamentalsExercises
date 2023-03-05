def drive(current_car, distance, needed_fuel):
    if current_car in cars:
        if needed_fuel <= cars[current_car]['fuel']:
            cars[current_car]['mileage'] += distance
            cars[current_car]['fuel'] -= needed_fuel
            print(f"{current_car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
            if cars[current_car]['mileage'] >= 100000:
                del cars[current_car]
                print(f"Time to sell the {current_car}!")
        else:
            print("Not enough fuel to make that ride")


def refuel(current_car, given_fuel):
    if current_car in cars:
        starting_fuel = cars[current_car]['fuel']
        cars[current_car]['fuel'] += given_fuel
        if cars[current_car]['fuel'] > 75:
            cars[current_car]['fuel'] = 75
            print(f"{current_car} refueled with {(75 - starting_fuel)} liters")
        else:
            print(f"{current_car} refueled with {given_fuel} liters")


def revert(current_car, kilometers):
    if current_car in cars:
        if cars[current_car]['mileage'] - kilometers <= 10000:
            cars[current_car]['mileage'] = 10000
        else:
            cars[current_car]['mileage'] -= kilometers
            print(f"{current_car} mileage decreased by {kilometers} kilometers")


number_of_cars = int(input())
cars = {}
for c in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {'mileage': int(mileage), 'fuel': int(fuel)}
command = input()
while command != "Stop":
    current_command = command.split(" : ")
    if current_command[0] == "Drive":
        drive(current_command[1], int(current_command[2]), int(current_command[3]))
    elif current_command[0] == "Refuel":
        refuel(current_command[1], int(current_command[2]))
    elif current_command[0] == "Revert":
        revert(current_command[1], int(current_command[2]))
    command = input()
for car in cars:
    print(f"{car} -> Mileage: {cars[car]['mileage']} kms, Fuel in the tank: {cars[car]['fuel']} lt.")
