number_of_rooms_in_centre = int(input())
is_chairs_not_enough = True
chairs_counter = 0
total_chairs = 0
total_people = 0
for room in range(1, number_of_rooms_in_centre + 1):
    data = input().split()
    chairs = len(data[0])
    people = int(data[1])
    total_chairs += chairs
    total_people += people

    if chairs < people:
        is_chairs_not_enough = False
        needed_chairs_in_room = abs(people - chairs)
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
    elif total_chairs > total_people:
        chairs_counter += abs(chairs - people)

if is_chairs_not_enough:
    print(f"Game On, {chairs_counter} free chairs left")